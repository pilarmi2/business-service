from typing import Annotated

from fastapi import Body

from src.models.score import router
from src.models.score import Score
from src.models.standard_response import StandardResponse


@router.get('')
async def search_score(
        municipality_id: str,
        period: str
):
    return Score(municipality_id=municipality_id, score=156.2, period=period)
