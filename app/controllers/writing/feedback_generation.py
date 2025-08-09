from utils.feedback_general_prompt import generate_feedback
import os

def generate_writing_feedback(exercise: str, user_input: str, grammar_points: str, twists: str) -> str:
    current_dir = os.path.dirname(__file__)
    template_path = os.path.join(current_dir, "feedback_template.txt")    

    return generate_feedback(exercise, grammar_points, user_input, template_path, twists)