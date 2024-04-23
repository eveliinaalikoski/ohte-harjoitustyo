import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete()
        self.user_berta = User("berta", "1234")
        self.user_marta = User("marta", "4321")

    def test_get_all(self):
        user_repository.create(self.user_berta)
        user_repository.create(self.user_marta)
        users = user_repository.get_all()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0][0], self.user_berta.username)
        self.assertEqual(users[1][0], self.user_marta.username)

    def test_create(self):
        user_repository.create(self.user_berta)
        users = user_repository.get_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][0], self.user_berta.username)

    def test_find_by_username_if_user(self):
        user_repository.create(self.user_marta)
        user = user_repository.find_by_username(self.user_marta.username)
        self.assertEqual(user.username, self.user_marta.username)

    def test_find_by_username_if_not_user(self):
        user = user_repository.find_by_username(self.user_berta.username)
        self.assertEqual(user, None)
