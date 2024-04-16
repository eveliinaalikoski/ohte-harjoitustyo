from entities.budget import Budget
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository)
from repositories.budget_repository import (
    budget_repository as default_budget_repository)


class InvalidCredentialsError(Exception):
    pass


class UsernameAlreadyExistsError(Exception):
    pass


class BudgetService:
    def __init__(self,
                 user_repository=default_user_repository,
                 budget_repository=default_budget_repository):
        self._user = None
        self._budget_repository = budget_repository
        self._user_repository = user_repository

    def get_current_user(self):
        return self._user

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = User(username, password)
        return user

    def register(self, username, password, login=True):
        user_exists = self._user_repository.find_by_username(username)
        if user_exists:
            raise UsernameAlreadyExistsError("Username is already taken")
        user = self._user_repository.create(User(username, password))
        self._user = User(username, password)
        return user

    def logout(self):
        self._user = None
        return self._user

    def get_budgets(self):
        budgets = self._budget_repository.find_by_username(self._user.username)
        return budgets

    def create_budget(self, budget_name):
        budget = Budget(name=budget_name,
                        username=self._user.username)
        return self._budget_repository.create_budget(budget)

    def get_budget_info(self, budget_name, username):
        x = self._budget_repository.get_by_budget_name(budget_name, username)
        print(x)
        return x[0]

    # DO LATER (in csv or move to sql???)
    # def update_budget(self, budget_name,
    #                   income,
    #                   rent,
    #                   groceries,
    #                   transportation,
    #                   hobbies):
    #     budget =


budget_service = BudgetService()
