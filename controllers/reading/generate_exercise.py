import os
from utils.GeneralPromptGen import generate_prompt_with_template



def generate_reading_exercise(dynamic_block: str) -> str:


    current_dir = os.path.dirname(__file__)
    template_path = os.path.join(current_dir, "reading_prompt.txt")

    return generate_prompt_with_template(dynamic_block, template_path)


if __name__ == "__main__":
    print("🧪 Running test:")
    test_block = "A short story about a family trip in the past. Include 5 true/false questions."
    print(generate_reading_exercise(test_block))