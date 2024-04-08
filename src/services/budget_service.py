from entities.budget import Budget
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository)
# from repositories.budget_repository import (
#     budget_repository as default_budget_repository)

class InvalidCredentialsError(Exception):
    pass

class UsernameAlreadyExistsError(Exception):
    pass

class BudgetService:
    def __init__(self,
                 user_repository = default_user_repository):
        self._user = None
        # self._budget_repository = budget_repository
        self._user_repository = user_repository

    
    def login(self, username, password):
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user
        return user
    
    def register(self, username, password, login = True):
        user_exists = self._user_repository.find_by_username(username)
        if user_exists:
            raise UsernameAlreadyExistsError("Username is already taken")
        user = self._user_repository.create(User(username, password))
        if login:
            self._user = user
        return user
    
budget_service = BudgetService()