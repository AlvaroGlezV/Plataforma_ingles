import openai
import os
from dotenv import load_dotenv  

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Inicializar cliente
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_feedback(Exercise: str, user_input: str, grammar_points: str,  template_path: str, twists: str = "") -> str:
    
    # Read the feedback template from the specified path
    with open(template_path, "r", encoding="utf-8") as file:
        feedback_template = file.read()

     # Rellenar placeholders
    feedback_prompt = (
        feedback_template
        .replace("{{EXERCISE}}", Exercise)
        .replace("{{USER_INPUT}}", user_input)
        .replace("{{GRAMMAR_POINTS}}", grammar_points)
        .replace("{{TWISTS}}", twists if twists else "")
    )
    feedback_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": feedback_prompt}
        ]
    )
    print(Exercise, user_input, grammar_points, template_path, twists)   

    return feedback_response.choices[0].message.content.strip()
