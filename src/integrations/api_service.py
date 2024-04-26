import json
import os
from typing import List

import requests

from src.models.income_statement import IncomeStatement
from src.models.loan_statement import LoanStatement
from src.models.municipality import Municipality


class ApiService:
    def __init__(self):
        """
        Initialize ApiService class.
        """
        self.__url = os.environ["API_SERVICE"]

    def get_municipality(self, municipality_id: str) -> Municipality:
        """
        Get municipality data by ID from the API.

        Args:
            municipality_id (str): The ID of the municipality.

        Returns:
            Municipality: Object representing the municipality data.
        """
        response = requests.get(self.__url + "/municipalities/" + municipality_id)

        return Municipality(**response.json())

    def get_income_statement(self, municipality_id: str, period: str) -> IncomeStatement:
        """
        Get income statement data by municipality ID and period from the API.

        Args:
            municipality_id (str): The ID of the municipality.
            period (str): The period for the income statement.

        Returns:
            IncomeStatement: Object representing the income statement data.
        """
        response = requests.get(f"{self.__url}/municipalities/{municipality_id}/incomeStatement?period={period}")

        return IncomeStatement(**response.json())

    def get_loans_statements(self, municipality_id: str, period: str) -> List[LoanStatement]:
        """
        Get loan statements data by municipality ID and period from the API.

        Args:
            municipality_id (str): The ID of the municipality.
            period (str): The period for the loan statements.

        Returns:
            List[LoanStatement]: List of loan statement objects.
        """
        response = requests.get(f"{self.__url}/municipalities/{municipality_id}/loansStatements?period={period}")

        data = json.loads(response.text)

        return [LoanStatement(**item) for item in data]
