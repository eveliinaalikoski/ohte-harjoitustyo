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
        info = self._budget_repository.get_by_budget_name(budget_name, username)
        print(list(info))
        return list(info)

    def update_budget(self, budget_name, 
                      username,
                      income,
                      rent,
                      groceries,
                      transportation,
                      hobbies):
        self._budget_repository.update_budget(budget_name,
                                              username,
                                              income,
                                              rent,
                                              groceries,
                                              transportation,
                                              hobbies)
        
    def check_budget_name(self, budget_name):
        list = self._budget_repository._get_all()
        print(list)
        for l in list:
            part = l.split(";")
            if budget_name == part[0]:
                return False
        return True
    
    def add_topic(self, budget_name, topic_entry):
        self._budget_repository.add_topic(budget_name, topic_entry)

    def update_topics(self, budget_name, topic, amount):
        self._budget_repository.update_topic(budget_name, topic, amount)
    
    def get_topics(self, budget_name):
        topics = self._budget_repository.get_topics(budget_name)
        return topics

budget_service = BudgetService()
