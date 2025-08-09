import openai
import os
from utils.feedback_general_prompt import generate_feedback
import json

# Llamar a la API para recibir retroalimentación

def generate_reading_feedback(reading_text, user_answers, grammar_points):
    current_dir = os.path.dirname(__file__)
    template_path = os.path.join(current_dir, "feedback_prompt.txt")

    print ("Generating feedback with the following parameters:" 
           f"\nExercise: {reading_text}"
           f"\nUser Input: {user_answers}"
           f"\nGrammar Points: {grammar_points}"
           f"\nTemplate Path: {template_path}")
    
    feedback = generate_feedback(
        Exercise=reading_text,
        user_input=user_answers,
        grammar_points=grammar_points,
        template_path=template_path,
    )
    return json.dumps({"feedback": feedback})
