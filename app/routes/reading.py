from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List

from app.controllers.reading.generate_exercise import generate_reading_exercise
from app.controllers.reading.generate_feedback import generate_reading_feedback

router = APIRouter(prefix="/reading", tags=["reading"])

# ✅ Modelos de request
class ReadingExerciseRequest(BaseModel):
    grammar_points: str

class ReadingFeedbackRequest(BaseModel):
    reading_text: str
    user_responses: list[dict[str, str]]  # List of question-answer pairs from the user
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
    print(req)
    try:
        # Convert user_answers dict to a string with line breaks
        if isinstance(req.user_responses, list):
            user_responses_str = "\n".join(
                f"{item['question']}: {item['answer']}" for item in req.user_responses
            )
        else:
            user_responses_str = str(req.user_responses)

        feedback = generate_reading_feedback(
            reading_text=req.reading_text,
            user_answers=user_responses_str,
            grammar_points=req.grammar_points,
        )
        return {"feedback": feedback}
    except Exception as e:
        import traceback
        print("Error generating feedback:", e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
