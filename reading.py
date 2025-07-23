import openai
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Crear cliente OpenAI
client = openai.OpenAI(api_key=api_key)

# Instrucciones para generar el ejercicio
reading_prompt = """
You are an English teacher assistant for CEFR level A2 learners.

Create a reading comprehension activity for teenagers or young adults at CEFR A2 level.

The activity must include:
- A reading text of approximately 350 words.
- Use accessible vocabulary, short sentences, and a narrative or informative tone.
- The grammar focus should be on past simple, present simple, and future with “going to”.
- Choose a realistic or interesting topic for young people: daily life, school, travel, family, hobbies, a fun experience, a dream, etc.

Then, write 12 comprehension questions:
- Include a mix of wh-questions (Who, What, Where, When, Why, How), true/false questions, and at least 2 multiple choice (A, B, or C).
- Make sure the questions cover general understanding and some specific details.

End with 2 helpful grammar or vocabulary tips for students.

Use this format:

---
**Reading Text**:  
...

**Questions**:  
1. ...  
2. ...  
... (until 12)

**Tips**:  
- ...
- ...
"""

# Llamar a la API para generar el ejercicio
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": reading_prompt}
    ]
)

# Mostrar el ejercicio generado
exercise = response.choices[0].message.content.strip()
print("\n📖 READING EXERCISE:\n")
print(exercise)

# Pedir respuestas del estudiante
student_response = input("\n✏️ Escribe tus respuestas aquí (puedes escribir en inglés o solo numerar las respuestas):\n")

# Crear prompt para pedir retroalimentación
feedback_prompt = f"""
You are an English teacher specialized in CEFR A2 reading comprehension.

The student has completed the following 12-question reading comprehension activity and submitted these answers:

{student_response}

Please:
- Check if each answer is correct or incorrect (based on a typical good student response).
- Give brief, friendly feedback in English.
- Mention 2–3 strengths and 1–2 improvement suggestions.
- End with an overall score: Excellent, Good, or Needs improvement.
"""

# Llamar a la API para recibir retroalimentación
feedback_response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": feedback_prompt}
    ]
)

# Mostrar retroalimentación
feedback = feedback_response.choices[0].message.content.strip()
print("\n📘 FEEDBACK:\n")
print(feedback)
