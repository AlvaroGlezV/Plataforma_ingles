from controllers.writing.generate_exercise import generate_writing_exercise
from controllers.writing.feedback_generation import generate_writing_feedback

def simulate_user_writing():
    # User input for grammar points
    grammar_points = input("🧑 Ingresa los puntos gramaticales a practicar (ej: Past simple, Present perfect):\n> ")

    # Generate a writing exercise
    exercise_json = generate_writing_exercise(grammar_points)

    Instructions = exercise_json["instruction"]
    email        = exercise_json["prompt"]
    twists       = exercise_json["twists"]  # this is a list

    print("\n 📜 Instrucciones del ejercicio: ", Instructions)
    print("\n ✉️ Ejercicio de escritura:\n", email)
    print("\n 🔄 Condiciones extra (twists): ", twists)

    # User input for answer
    user_answer = input("\n🧑 Escribe tu respuesta al ejercicio:\n> ")

    # --- NEW: format twists as a single string ---
    twists_str = "\n".join(f"- {t}" for t in twists)

    # Generate feedback (now passing a string, not a list)
    feedback = generate_writing_feedback(
        exercise=f"{Instructions}\n{email}",
        grammar_points=grammar_points,
        user_input=user_answer,
        twists=twists_str
    )

    print("\n📝 Feedback generado:\n", feedback)

if __name__ == "__main__":
    simulate_user_writing()
