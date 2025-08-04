import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargar la clave desde el archivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generate_prompt_response(DynamicBlock: str):
    # Cargar plantilla desde archivo de texto
    with open("PromptSituationSp.txt", "r", encoding="utf-8") as file:
        template = file.read()

    # Reemplazar el bloque dinámico en la plantilla
    prompt = template.replace("{{DYNAMIC_BLOCK}}", DynamicBlock)

    # Llamar a la API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": prompt
            }
        ]
    )

    # Devolver el contenido como texto
    return response.choices[0].message.content.strip()
