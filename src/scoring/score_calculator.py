from typing import List

from src.models.income_statement import IncomeStatement
from src.models.loan_statement import LoanStatement
from src.models.municipality import Municipality
from src.models.score import Score


class ScoreCalculator:
    def calculate_score(self, municipality: Municipality = None,
                        income_statement: IncomeStatement = None,
                        loans_statements: List[LoanStatement] = None) -> Score:
        score: float = 0.0

        citizens: int = municipality.citizens
        assets: float = income_statement.assets
        passives: float = income_statement.passives
        aggregated_loans: float = 0.0

        for loan in loans_statements:
            aggregated_loans += (loan.drawn_amount - loan.repaid_amount)

        score = round(max(1, (passives + aggregated_loans - assets) / citizens), 2)

        return Score(municipality_id=municipality.municipality_id, score=score, period=income_statement.period)
