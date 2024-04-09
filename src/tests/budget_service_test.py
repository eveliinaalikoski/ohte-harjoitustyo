import unittest
from services.budget_service import BudgetService
from entities.user import User

class UserRepositoryTests:
    def __init__(self, users = None):
        self.users = users or []
    
    def create(self, user):
        self.users.append(user)
        return user

    def find_by_username(self, username):
        users = filter(lambda user: user.username == username, self.users)
        users_list = list(users)
        return users_list[0] if len(users_list)>0 else None


class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.budget_service = BudgetService(UserRepositoryTests())
        self.user_test = User("test", "test123")
    
    def login_user(self, user):
        self.budget_service.register(user.username, user.password)

    def test_login_with_right_credentials(self):
        self.budget_service.register(self.user_test.username,
                                     self.user_test.password)
        user = self.budget_service.login(self.user_test.username,
                                         self.user_test.password)
        self.assertEqual(user.username, self.user_test.username)

    