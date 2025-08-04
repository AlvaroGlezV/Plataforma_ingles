import openai
import os
from utils.feedback_general_prompt import generate_feedback

# Llamar a la API para recibir retroalimentación

def generate_feedback(DynamicBlock: str):
    
    current_dir = os.path.dirname(__file__)
    prompt_path = os.path.join(current_dir, "feedback_prompt.txt")

    with open(prompt_path, "r", encoding="utf-8") as file:
        feedback_template = file.read()
    feedback_prompt = feedback_template.replace("{{DYNAMIC_BLOCK}}", DynamicBlock)

    feedback_response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": feedback_prompt}
    ]
)
    return feedback_response.choices[0].message.content.strip()

def generate_reading_feedback(exercise, user_input, grammar_points, twists=""):
    current_dir = os.path.dirname(__file__)
    template_path = os.path.join(current_dir, "feedback_prompt.txt")
    return generate_feedback(
        Exercise=exercise,
        user_input=user_input,
        grammar_points=grammar_points,
        template_path=template_path,
        twists=twists
    )
