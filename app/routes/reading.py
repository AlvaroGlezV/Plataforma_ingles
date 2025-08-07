from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List

from controllers.reading.generate_exercise import generate_reading_exercise
from controllers.reading.generate_feedback import generate_reading_feedback

router = APIRouter(prefix="/reading", tags=["reading"])

# ✅ Modelos de request
class ReadingExerciseRequest(BaseModel):
    grammar_points: str

class ReadingFeedbackRequest(BaseModel):
    reading_text: str
    questions: list
    user_answers: list
    grammar_points: str

#Endpoint: Generar ejercicio dinámico de lectura
@router.post("/exercise")
async def reading_exercise(req: ReadingExerciseRequest):
    try:
        reading = generate_reading_exercise(req.grammar_points)
        return reading  # JSON: reading_text, questions, tips
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#Endpoint: Generar feedback sobre respuestas del usuario
@router.post("/feedback")
async def reading_feedback(req: ReadingFeedbackRequest):
    try:
        feedback = generate_reading_feedback(
            reading_text=req.reading_text,
            questions=req.questions,
            user_answers=req.user_answers,
            grammar_points=req.grammar_points,
        )
        return {"feedback": feedback}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
