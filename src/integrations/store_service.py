import json
import os
from typing import List

import requests

from src.models.income_statement import IncomeStatement
from src.models.loan_statement import LoanStatement
from src.models.municipality import Municipality
from src.models.score import Score
from src.models.standard_response import StandardResponse


class StoreService:
    def __init__(self):
        """
        Initialize StoreService class.
        """
        self.__url = os.environ["STORE_SERVICE"]

    def get_municipality(self, municipality_id: str) -> Municipality:
        response = requests.get(self.__url + "/municipalities/" + municipality_id)

        if response.text != "null":
            return Municipality(**response.json())
        else:
            return None

    def get_income_statement(self, municipality_id: str, period: str) -> IncomeStatement:
        response = requests.get(f"{self.__url}/municipalities/{municipality_id}/incomeStatement?period={period}")

        if response.text != "null":
            return IncomeStatement(**response.json())
        else:
            return None

    def get_loans_statements(self, municipality_id: str, period: str) -> List[LoanStatement]:
        response = requests.get(f"{self.__url}/municipalities/{municipality_id}/loansStatements?period={period}")

        data = json.loads(response.text)

        return [LoanStatement(**item) for item in data]

    def get_score(self, municipality_id: str, period: str) -> Score:
        response = requests.get(f"{self.__url}/municipalities/{municipality_id}/score?period={period}")

        if response.text != "null":
            return Score(**response.json())
        else:
            return None

    def post_score(self, score: Score) -> StandardResponse:
        response = requests.post(self.__url + f"/municipalities/{score.municipality_id}/score",
                                 data=score.json())
        print(response.text)
        return StandardResponse(status=response.status_code, message=response.text)
