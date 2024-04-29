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
    """class responsible for app logic"""

    def __init__(self,
                 user_repository=default_user_repository,
                 budget_repository=default_budget_repository):
        """class constructor, creates new service for app logic

        Args:
            user_repository (optional): 
                Defaults to UserRepository-object.
                Object having UserRepository-class methods.
            budget_repository (optional): 
                Defaults to BudgetRepository-object.
                Object having BudgetRepository-class methods.
        """
        self._budget_repository = budget_repository
        self._user_repository = user_repository
        self._user = None

    def get_current_user(self):
        """Returns logged in user

        Returns:
            Object: User-object of user that is logged in
        """
        return self._user

    def login(self, username, password):
        """logs user in

        Args:
            username (str-object): unique username
            password (str-object): password that matches username

        Raises:
            InvalidCredentialsError: error, if username not registered

        Returns:
            Object: logged in user as User-object
        """
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = User(username, password)
        return user

    def register(self, username, password):
        """Creates new user and logs them in

        Args:
            username (str-object): unique username
            password (str-object): password for user

        Raises:
            UsernameAlreadyExistsError: error, if username is already taken

        Returns:
            Object: logged in user as User-object
        """
        user_exists = self._user_repository.find_by_username(username)
        if user_exists:
            raise UsernameAlreadyExistsError("Username is already taken")
        user = self._user_repository.create(User(username, password))
        self._user = User(username, password)
        return user

    def logout(self):
        """log out current user"""
        self._user = None

    def get_budgets(self):
        """returns user's created budgets

        Returns:
            list: list of Budget-objects
        """
        budgets = self._budget_repository.find_by_username(self._user.username)
        return budgets

    def create_budget(self, budget_name):
        """creates new budget

        Args:
            budget_name (str-string): unique name for budget
        """
        budget = Budget(name=budget_name,
                        username=self._user.username)
        self._budget_repository.create_budget(budget)

    def get_budget_info(self, budget_name, username):
        """returns budget information

        Args:
            budget_name (str-string): name of budget, where information is wanted
            username (str-string): username of user that owns the budget

        Returns:
            list: information that is saved about the budget
        """
        info = self._budget_repository.get_by_budget_name(
            budget_name, username)
        print(list(info))
        return list(info)

    def update_budget(self, budget_name,
                      username,
                      income,
                      rent,
                      groceries,
                      hobbies):
        self._budget_repository.update_budget(budget_name,
                                              username,
                                              income,
                                              rent,
                                              groceries,
                                              hobbies)

    def check_budget_name(self, budget_name):
        """check if a name for budget is free

        Args:
            budget_name (str-string): name for budget

        Returns:
            Boolean: boolean-value of if the name is free
        """
        budgets = self._budget_repository.get_all()
        for b in budgets:
            if type(b)==tuple:
                name = b[0]
            else:
                name = b.name
            if budget_name == name:
                return False
        return True

    def add_topic(self, budget_name, topic, amount):
        self._budget_repository.add_topic(budget_name, topic, amount)

    def get_topics(self, budget_name):
        topics = self._budget_repository.get_topics(budget_name)
        return topics


budget_service = BudgetService()
