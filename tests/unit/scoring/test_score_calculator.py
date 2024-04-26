import unittest

from src.models.income_statement import IncomeStatement
from src.models.municipality import Municipality
from src.scoring.score_calculator import ScoreCalculator


class TestScoreCalculator(unittest.TestCase):
    def test_calculate_score(self):
        score_calculator = ScoreCalculator()

        municipality = Municipality(municipality_id="1234", name="City", citizens=15966)
        income_statement = IncomeStatement(municipality_id="1234", assets=568965, passives=1235698, period="2023-12-31")
        score = score_calculator.calculate_score(municipality, income_statement, []).score
        assert score == 41.76
