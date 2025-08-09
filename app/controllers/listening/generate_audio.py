from melo.api import TTS
import sys
import os
import uuid
import shlex

def main():
    # Asegurarse de que el texto venga correctamente parseado si contiene espacios o comillas
    texto = sys.argv[1] if len(sys.argv) > 1 else "This is a test audio from MeloTTS."

    # Generar nombre único
    nombre = f"output_{uuid.uuid4().hex[:6]}.wav"
    ruta_salida = os.path.join("/app/audio", nombre)

    # Crear carpeta si no existe
    os.makedirs("/app/audio", exist_ok=True)

    # Instanciar el modelo
    tts = TTS(language='EN', device='cpu')

    # Generar el audio
    tts.tts_to_file(texto, speaker_id=0, output_path=ruta_salida)

    # Imprimir nombre y ruta para que el backend pueda capturarlos si es necesario
    print(f"✅ Audio generado en {ruta_salida}")
    print(nombre)

if __name__ == "__main__":
    main()