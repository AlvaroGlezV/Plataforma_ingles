import openai
import os
from dotenv import load_dotenv
import json
import re

# Cargar variables de entorno desde el archivo .env
load_dotenv(override=True)


# Crear cliente OpenAI
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Llamar a la API para generar el ejercicio
def generate_prompt_with_template(dynamic_block: str, template_path: str, debug: bool = True) -> dict:
    """
    Loads a prompt template from a file, inserts the dynamic block, and sends it to OpenAI.

    Args:
        dynamic_block (str): Text to replace the {{DYNAMIC_BLOCK}} placeholder in the template.
        template_path (str): Path to the .txt template file.

    Returns:
        str: Cleaned response text from OpenAI.
    """

    # Validate that the template file exists
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template not found at path: {template_path}")

    with open(template_path, "r", encoding="utf-8") as file:
        file_content = file.read()

    prompt = file_content.replace("{{DYNAMIC_BLOCK}}", dynamic_block)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": prompt}]
    )

    raw_text = response.choices[0].message.content.strip()
    finish_reason = response.choices[0].finish_reason
    usage = dict(response.usage)

    if debug:
        print("\n🧠 --- DEBUG OUTPUT ---")
        print("📄 Prompt:\n", prompt)
        print("📥 Raw model output:\n", raw_text)
        print("⛔ Finish reason:", finish_reason)
        print("📊 Token usage:", usage)
        print("----------------------\n")

    if raw_text.startswith("```"):
        # Remove ```json or ``` and ending ```
        raw_text = re.sub(r"^```[a-zA-Z]*\n?", "", raw_text)
        raw_text = re.sub(r"\n?```$", "", raw_text)

    # Now parse as JSON
    try:
        parsed_json = json.loads(raw_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"❌ Failed to parse model output as JSON. Output was:\n{raw_text[:300]}") from e

    return parsed_json


