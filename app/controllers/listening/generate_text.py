import os
from utils.GeneralPromptGen import generate_prompt_with_template

def generate_listening_exercise(dynamic_block: str) -> str:
    current_dir = os.path.dirname(__file__)
    template_path = os.path.join(current_dir, "listening_prompt.txt")
    return generate_prompt_with_template(dynamic_block, template_path)

if __name__ == "__main__":
    print("🧪 Running test:")
    test_block = "A conversation between two friends planning a weekend trip. Make it suitable for B1 level students."
    print(generate_listening_exercise(test_block))
