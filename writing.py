import openai
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env (ubicado en el directorio superior)
load_dotenv(dotenv_path="../.env")

# Verificar si la variable se cargó correctamente
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ ERROR: No se encontró la variable OPENAI_API_KEY. Verifica que el archivo .env exista y esté correctamente escrito.")
    exit()

# Crear cliente OpenAI
client = openai.OpenAI(api_key=api_key)

# Mostrar instrucciones al estudiante
print("\n✍️ WRITING TASK:")
print("""
Write a short paragraph (6–8 sentences) in English about **your favorite hobby**, a recent trip, or a fun memory.
Try to use past simple, present simple, and future (going to) if possible.

Example topics:
- My favorite video game
- A trip I took with my family
- What I'm going to do next weekend
""")

# Recoger el texto del alumno
student_text = input("\n📝 Write your paragraph below:\n")

# Prompt para retroalimentación de escritura
writing_feedback_prompt = f"""
You are an English teacher for CEFR A2 level students.

The student wrote the following paragraph in English:

{student_text}

Please do the following:
- Correct any grammar, vocabulary or spelling errors (in a friendly way).
- Provide a corrected version of the paragraph.
- Give a short explanation of 2–3 common mistakes (in simple English).
- End with a final comment to encourage the student.
"""

# Llamar a la API para obtener retroalimentación
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": writing_feedback_prompt}
    ]
)

# Mostrar la retroalimentación
feedback = response.choices[0].message.content.strip()
print("\n📘 WRITING FEEDBACK:\n")
print(feedback)
