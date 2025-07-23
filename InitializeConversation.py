import os
import threading
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation, ConversationInitiationData
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

load_dotenv()

def start_conversation_session(prompt_text: str):
    # Leer credenciales
    agent_id = os.getenv("AGENT_ID")
    api_key = os.getenv("ELEVENLABS_API_KEY")

    # Configuración dinámica del prompt
    override_config = ConversationInitiationData(
    conversation_config_override={
        "agent": {
            "prompt": {
                "prompt": prompt_text
            },
            "language": "en",
        },
        "tts": {
            "voice_id": "21m00Tcm4TlvDq8ikWAM"
        }
    }
)


    # Inicializar cliente
    elevenlabs = ElevenLabs(api_key=api_key)

    # Crear conversación
    conversation = Conversation(
    client=elevenlabs,
    agent_id=agent_id,
    requires_auth=True,
    config=override_config,
    audio_interface=DefaultAudioInterface(),
    callback_user_transcript=lambda t: print(f"\n🧍 You: {t}"),
    callback_agent_response=lambda r: print(f"🤖 Agent: {r}"),
)

    # Hilo separado para la conversación
    def _start():
        conversation.start_session()
        conversation.wait_for_session_end()

    thread = threading.Thread(target=_start)
    thread.start()

    try:
        while thread.is_alive():
            user_input = input("\nPresiona 'q' y Enter para terminar la sesión: ")
            if user_input.lower() == 'q':
                print("⏹️ Finalizando conversación...")
                conversation.end_session()
                break
    except KeyboardInterrupt:
        print("\n🛑 Interrupción detectada. Cerrando sesión.")
        conversation.end_session()

    thread.join()

# Si este archivo se ejecuta directamente, usa un prompt por defecto
if __name__ == "__main__":
    default_prompt = "You are a friendly and encouraging English tutor. Give short, clear answers and always ask a follow-up question."
    start_conversation_session(default_prompt)
