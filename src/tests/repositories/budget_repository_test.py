import unittest
from repositories.budget_repository import budget_repository
from repositories.user_repository import user_repository
from entities.budget import Budget
from entities.user import User


class TestBudgetRepository(unittest.TestCase):
    def setUp(self):
        budget_repository.delete()
        user_repository.delete()
        self.user_berta = User("berta", "1234")
        self.user_marta = User("marta", "4321")
        self.budget1 = Budget("uno", self.user_berta.username)
        self.budget2 = Budget("dos", self.user_marta.username)

    def test_find_by_username(self):
        budgets = budget_repository.find_by_username(self.user_berta.username)
        self.assertEqual(len(budgets), 0)

        budget_repository.create_budget(self.budget1)
        budgets = budget_repository.find_by_username(self.user_berta.username)
        self.assertEqual(len(budgets), 1)

    def test_get_by_budget_name(self):
        budget_repository.create_budget(self.budget1)
        budget = budget_repository.get_by_budget_name(
            self.budget1.name, self.user_berta.username)
        self.assertEqual(len(budget), 6)

    def test_check_budget_name_nonexisting_name(self):
        ok = budget_repository.check_budget_name(self.budget1.name)
        self.assertEqual(ok, True)

    def test_check_budget_name_existing_name(self):
        budget_repository.create_budget(self.budget1)
        ok = budget_repository.check_budget_name(self.budget1.name)
        self.assertEqual(ok, False)

    def test_update_budget(self):
        budget_repository.create_budget(self.budget1)
        budget_repository.update_budget(self.budget1.name, self.budget1.username,
                                        1, 2, 3, 4)
        budget = budget_repository.get_by_budget_name(
            self.budget1.name, self.budget1.username)
        self.assertEqual(budget[2], 1)
        self.assertEqual(budget[3], 2)
        self.assertEqual(budget[4], 3)
        self.assertEqual(budget[5], 4)

    def test_add_topic(self):
        budget_repository.create_budget(self.budget2)
        budget_repository.add_topic(self.budget2.name, "topic", 0)
        topics = budget_repository.get_topics(self.budget2.name)
        self.assertEqual(len(topics), 1)

    def test_delete(self):
        budget_repository.create_budget(self.budget1)
        budgets = budget_repository.get_all()
        self.assertEqual(len(budgets), 1)
        budget_repository.delete()
        budgets = budget_repository.get_all()
        self.assertEqual(len(budgets), 0)
