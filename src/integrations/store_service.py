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
        """
        Get municipality data by ID from the store service.

        Args:
            municipality_id (str): The ID of the municipality.

        Returns:
            Municipality or None: Object representing the municipality data, or None if not found.
        """
        response = requests.get(self.__url + "/municipalities/" + municipality_id)

        if response.text != "null":
            return Municipality(**response.json())
        else:
            return None

    def get_income_statement(self, municipality_id: str, period: str) -> IncomeStatement:
        """
        Get income statement data by municipality ID and period from the store service.

        Args:
            municipality_id (str): The ID of the municipality.
            period (str): The period for the income statement.

        Returns:
            IncomeStatement or None: Object representing the income statement data, or None if not found.
        """
        response = requests.get(f"{self.__url}/municipalities/{municipality_id}/incomeStatement?period={period}")

        if response.text != "null":
            return IncomeStatement(**response.json())
        else:
            return None

    def get_loans_statements(self, municipality_id: str, period: str) -> List[LoanStatement]:
        """
        Get loan statements data by municipality ID and period from the store service.

        Args:
            municipality_id (str): The ID of the municipality.
            period (str): The period for the loan statements.

        Returns:
            List[LoanStatement]: List of loan statement objects.
        """
        response = requests.get(f"{self.__url}/municipalities/{municipality_id}/loansStatements?period={period}")

        data = json.loads(response.text)

        return [LoanStatement(**item) for item in data]

    def get_score(self, municipality_id: str, period: str) -> Score:
        """
        Get score data by municipality ID and period from the store service.

        Args:
            municipality_id (str): The ID of the municipality.
            period (str): The period for the score.

        Returns:
            Score or None: Object representing the score data, or None if not found.
        """
        response = requests.get(f"{self.__url}/municipalities/{municipality_id}/score?period={period}")

        if response.text != "null":
            return Score(**response.json())
        else:
            return None

    def post_score(self, score: Score) -> StandardResponse:
        """
        Post score data to the store service.

        Args:
            score (Score): Object representing the score data to be posted.

        Returns:
            StandardResponse: Object representing the response from the store service.
        """
        response = requests.post(self.__url + f"/municipalities/{score.municipality_id}/score",
                                 data=score.json())
        print(response.text)
        return StandardResponse(status=response.status_code, message=response.text)
