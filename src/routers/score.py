from http import HTTPStatus
from typing import Annotated, List

from fastapi import Body

from src.integrations.api_service import ApiService
from src.integrations.store_service import StoreService
from src.models.income_statement import IncomeStatement
from src.models.loan_statement import LoanStatement
from src.models.municipality import Municipality
from src.models.score import router
from src.models.score import Score
from src.models.standard_response import StandardResponse
from src.scoring.score_calculator import ScoreCalculator

store_service: StoreService = StoreService()
api_service: ApiService = ApiService()


@router.get('')
async def search_score(
        municipality_id: str,
        period: str
):
    score: Score = store_service.get_score(municipality_id, period)

    if score is not None:
        return score

    municipality: Municipality = store_service.get_municipality(municipality_id)
    income_statement: IncomeStatement = store_service.get_income_statement(municipality_id, period)
    loans_statements: List[LoanStatement] = store_service.get_loans_statements(municipality_id, period)

    if municipality is None:
        municipality = api_service.get_municipality(municipality_id)

    if income_statement is None:
        income_statement = api_service.get_income_statement(municipality_id, period)

    if not loans_statements:
        loans_statements = api_service.get_loans_statements(municipality_id, period)

    if municipality is not None and income_statement is not None:
        score = ScoreCalculator().calculate_score(municipality=municipality,
                                                  income_statement=income_statement,
                                                  loans_statements=loans_statements)

        store_service.post_score(score)
        return score
    else:
        return StandardResponse(status=HTTPStatus.BAD_REQUEST, message='Bad request')
