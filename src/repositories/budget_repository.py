from entities.budget import Budget
from repositories.user_repository import user_repository
from config import BUDGET_FILE_PATH
from pathlib import Path

class BudgetRepository:
    def __init__(self, file_path):
        self._file_path = file_path
    
    def _get_all(self):
        return self._read()

    def find_by_username(self, username):
        budgets = self._get_all()
        own_budgets = []
        for row in budgets:
            part = row.split(";")
            budget_name = part[0]
            user = part[1]
            income = part[2]
            rent = part[3]
            if username == user:
                own_budgets.append(Budget(budget_name, 
                                      user, 
                                      income, 
                                      rent))
        return own_budgets

    def _file_exists(self):
        Path(self._file_path).touch()
    
    def _read(self):
        self._file_exists()
        budget_list = []
        with open(self._file_path) as file:
            for row in file:
                row = row.replace("\n", "")
                budget_list.append(row)
        return budget_list
    
    def create_budget(self, budget):
        budgets = self._get_all()
        budgets.append(budget)
        self._add(budget)
    
    def _add(self, budget):
        self._file_exists()
        name = budget.name
        username = budget.username
        income = str(budget.income)
        rent = str(budget.rent)
        with open(self._file_path, "a") as file:
            file.write((name)+";")
            file.write((username)+";")
            file.write((income)+";")
            file.write((rent)+"\n")

    def delete(self):
        with open(self._file_path, "w") as file:
            file.write("")

budget_repository = BudgetRepository(BUDGET_FILE_PATH)