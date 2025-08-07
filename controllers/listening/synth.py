import os
import openai


client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def synthesize_text(text: str, voice: str = "alloy") -> bytes:
    """Convert text to speech using an external TTS service and return audio bytes."""
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice=voice,
        input=text
    ) as response:
        audio_bytes = b"".join(response.iter_bytes())
    return audio_bytes


if __name__ == "__main__":
    print("🧪 Running test:")
    sample_audio = synthesize_text("Hello, this is a test of the text to speech system.")
    with open("sample_audio.mp3", "wb") as f:
        f.write(sample_audio)
    print("Sample audio written to sample_audio.mp3")
