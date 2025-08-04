import openai
from utils.GeneralPromptGen import generate_prompt_with_template
import os

# Generate a writing exercise based on a dynamic block of text

def generate_writing_exercise(dynamic_block: str) -> str:
    current_dir = os.path.dirname(__file__)
    template_path = os.path.join(current_dir, "prompt_template.txt")

    return generate_prompt_with_template(dynamic_block, template_path)


if __name__ == "__main__":
    print("🧪 Running test:")
    test_block = "- Past simple\n- Present perfect\n- Future simple"
    print(generate_writing_exercise(test_block))