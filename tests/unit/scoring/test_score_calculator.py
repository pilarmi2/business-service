import unittest

from src.scoring.score_calculator import ScoreCalculator


class TestScoreCalculator(unittest.TestCase):
    def test_calculate_score(self):
        score_calculator = ScoreCalculator()
        assert score_calculator.calculate_score().score == 156.2
