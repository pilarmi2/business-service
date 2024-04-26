from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/municipalities/{municipality_id}/score",
    tags=["Scoring"]
)


class Score(BaseModel):
    """
    Represents a score assigned to a municipality for a specific period.

    Attributes:
        municipality_id (int): The ID of the municipality.
        score (float): The score assigned to the municipality.
        period (str): The period for which the score is assigned.
    """
    municipality_id: str
    score: float
    period: str

