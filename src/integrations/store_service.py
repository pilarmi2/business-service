import json
import os
import requests

from src.models.income_statement import IncomeStatement
from src.models.loan_statement import LoanStatement
from src.models.municipality import Municipality
from src.models.standard_response import StandardResponse


class StoreService:
    def __init__(self):
        """
        Initialize StoreService class.
        """
        self.__url = os.environ["STORE_SERVICE"]

    def get_municipality(self, municipality_id: str):
        pass

    def get_income_statement(self, income_statement_id: str):
        pass

    def get_loans_statements(self, municipality_id: str, period: str):
        pass

    def get_score(self, municipality_id: str, period_id: str):
        pass

    def post_score(self, municipality_id: str, period_id: str):
        pass