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
        Initialize StoreService class.
        """
        self.__url = os.environ["API_SERVICE"]

    def get_municipality(self, municipality_id: str) -> Municipality:
        response = requests.get(self.__url + "/municipalities/" + municipality_id)

        return Municipality(**response.json())

    def get_income_statement(self, municipality_id: str, period: str) -> IncomeStatement:
        response = requests.get(f"{self.__url}/municipalities/{municipality_id}/incomeStatement?period={period}")

        return IncomeStatement(**response.json())

    def get_loans_statements(self, municipality_id: str, period: str) -> List[LoanStatement]:
        response = requests.get(f"{self.__url}/municipalities/{municipality_id}/loansStatements?period={period}")

        data = json.loads(response.text)

        return [LoanStatement(**item) for item in data]
