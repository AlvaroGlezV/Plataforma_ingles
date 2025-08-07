import os
from utils.GeneralPromptGen import generate_prompt_with_template


def generate_listening_exercise(dynamic_block: str) -> str:
    """Generate a listening exercise using a prompt template and dynamic block."""
    current_dir = os.path.dirname(__file__)
    template_path = os.path.join(current_dir, "listening_prompt.txt")
    return generate_prompt_with_template(dynamic_block, template_path)


if __name__ == "__main__":
    print("🧪 Running test:")
    test_block = "A short dialogue about ordering food at a restaurant. Include 3 questions."
    print(generate_listening_exercise(test_block))
