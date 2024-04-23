import unittest
from services.budget_service import (BudgetService,
                                     InvalidCredentialsError,
                                     UsernameAlreadyExistsError)
from entities.user import User
from entities.budget import Budget


class BudgetRepositoryTests:
    def __init__(self, budgets=None):
        self.budgets = budgets or []

    def get_all(self):
        return self.budgets

    def find_by_username(self, username):
        own_budgets = filter(
            lambda budget: budget.username == username, self.budgets)
        return list(own_budgets)

    def get_by_budget_name(self, budget_name, username):
        own_budget = filter(lambda budget: budget.name == budget_name
                            and budget.username == username, self.budgets)
        return own_budget

    def create_budget(self, budget):
        self.budgets.append(budget)
        return budget

    def delete(self):
        self.budgets = []


class UserRepositoryTests:
    def __init__(self, users=None):
        self.users = users or []

    def get_all(self):
        return self.users

    def create(self, user):
        self.users.append(user)
        return user

    def find_by_username(self, username):
        users = filter(lambda user: user.username == username, self.users)
        users_list = list(users)
        return users_list[0] if len(users_list) > 0 else None

    def delete(self):
        self.users = []


class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.budget_service = BudgetService(UserRepositoryTests(),
                                            BudgetRepositoryTests())
        self.user_test = User("test", "test123")
        self.budget1 = Budget("first", self.user_test.username)
        self.budget2 = Budget("second", self.user_test.username)

    def login_user(self, user):
        self.budget_service.register(user.username, user.password)

    def test_get_current_user(self):
        self.login_user(self.user_test)
        current = self.budget_service.get_current_user()
        self.assertEqual(current.username, self.user_test.username)

    def test_login_with_valid_credentials(self):
        self.budget_service.register(self.user_test.username,
                                     self.user_test.password)
        user = self.budget_service.login(self.user_test.username,
                                         self.user_test.password)
        self.assertEqual(user.username, self.user_test.username)

    def test_login_with_invalid_credentials(self):
        self.assertRaises(InvalidCredentialsError,
                          lambda: self.budget_service.login("invalid", "credentials"))

    def test_register_with_valid_credentials(self):
        username = self.user_test.username
        password = self.user_test.password
        self.budget_service.register(username, password)
        user = self.budget_service.login(username, password)
        self.assertEqual(user.username, self.user_test.username)

    def test_register_with_existing_username(self):
        username = self.user_test.username
        self.budget_service.register(username, "test")
        self.assertRaises(UsernameAlreadyExistsError,
                          lambda: self.budget_service.register(username, "lalala"))

    def test_logout(self):
        self.login_user(self.user_test)
        user = self.budget_service.logout()
        self.assertEqual(None, user)

    def test_get_budgets(self):
        self.login_user(self.user_test)
        self.budget_service.create_budget(self.budget1.name)
        self.budget_service.create_budget(self.budget2.name)
        budgets = self.budget_service.get_budgets()
        self.assertEqual(len(budgets), 2)
        self.assertEqual(budgets[0].name, self.budget1.name)

    def test_create_budget(self):
        self.login_user(self.user_test)
        self.budget_service.create_budget("testing")
        budgets = self.budget_service.get_budgets()
        self.assertEqual(len(budgets), 1)
        self.assertEqual(budgets[0].name, "testing")
        self.assertEqual(budgets[0].username, self.user_test.username)

    def test_budget_info(self):
        self.login_user(self.user_test)
        self.budget_service.create_budget(self.budget1.name)
        info = self.budget_service.get_budget_info(
            self.budget1.name, self.user_test.username)
        # self.assertEqual(info, [self.budget1.name,
        #                         self.user_test.username,
        #                         0, 0, 0, 0, 0])
        # self.assertEqual(info[1], self.budget1.username)
        # self.assertEqual(info[2], self.budget1.username)
        # self.assertEqual(info[3], self.budget1.username)
        # self.assertEqual()
