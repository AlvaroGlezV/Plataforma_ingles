from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

from controllers.writing.generate_exercise import generate_writing_exercise
from controllers.writing.feedback_generation import generate_writing_feedback

router = APIRouter(prefix="/writing", tags=["writing"])

# Request models
class ExerciseRequest(BaseModel):
    grammar_points: str

class FeedbackRequest(BaseModel):
    exercise: str
    user_input: str
    grammar_points: str
    twists: Optional[str] = ""

# Endpoints
@router.post("/exercise")
async def writing_exercise(req: ExerciseRequest):
    try:
        exercise = generate_writing_exercise(req.grammar_points)
        return {"exercise": exercise}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/feedback")
async def writing_feedback(req: FeedbackRequest):
    try:
        feedback = generate_writing_feedback(
            exercise=req.exercise,
            user_input=req.user_input,
            grammar_points=req.grammar_points,
            twists=req.twists or "",
        )
        return {"feedback": feedback}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
