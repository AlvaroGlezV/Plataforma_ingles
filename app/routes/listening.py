from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.controllers.listening.generate_text import generate_listening_exercise
from app.controllers.listening.generate_audio import generate_audio_from_text

router = APIRouter(prefix="/listening", tags=["listening"])

class AudioRequest(BaseModel):
    dynamic_block: str  # esto es lo que tú llamas dynamic_block en el template

@router.post("/listening/audio")
def generar_audio(req: AudioRequest):
    try:
        # 1. Generar texto con el prompt + template
        texto = generate_listening_exercise(req.dynamic_block)

        # 2. Generar audio con MeloTTS
        result = generate_audio_from_text(texto)

        return {
            "text": texto,
            **result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
