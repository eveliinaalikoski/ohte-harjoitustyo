from pathlib import Path
from entities.budget import Budget
from config import BUDGET_FILE_PATH
from database_connection import get_database_connection


class BudgetRepository:
    def __init__(self, file_path, connection):
        self._file_path = file_path
        self._connection = connection

    def get_all(self):
        return self._read()

    def find_by_username(self, username):
        budgets = self.get_all()
        own_budgets = []
        for row in budgets:
            part = row.split(";")
            budget_name = part[0]
            user = part[1]
            if username == user:
                own_budgets.append(Budget(budget_name, user))
        return own_budgets

    def get_by_budget_name(self, budget_name, username):
        cursor = self._connection.cursor()
        budget = cursor.execute("""SELECT * FROM budgets
                       WHERE name = ? AND username = ?""",
                                (budget_name, username)).fetchall()
        return budget[0]

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
        budgets = self.get_all()
        budgets.append(budget)
        print(budgets)
        self._add(budget)

    def _add(self, budget):
        self._file_exists()
        name = budget.name
        username = budget.username
        with open(self._file_path, "a") as file:
            file.write((name)+";")
            file.write((username)+"\n")

        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO budgets 
                       (name, username, income, rent, groceries, 
                       transportation, hobbies)
                       VALUES (?, ?, 0, 0, 0, 0, 0)""",
                       (name, username))
        self._connection.commit()

    def update_budget(self, budget_name, username, income, rent, groceries, transportation, hobbies):
        cursor = self._connection.cursor()
        cursor.execute("""UPDATE budgets
                       SET income = ?, rent = ?, groceries = ?, 
                       transportation = ?, hobbies = ?
                       WHERE name = ? AND username = ?""",
                       (income, rent, groceries, transportation, hobbies, budget_name, username))
        self._connection.commit()

    def add_topic(self, budget_name, topic):
        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO topics
                       (budget_name, topic, amount)
                       VALUES (?, ?, 0)""",
                       (budget_name, topic))
        self._connection.commit()

    def update_topic(self, budget_name, topic, amount):
        cursor = self._connection.cursor()
        cursor.execute("""UPDATE topics
                       SET amount = ?
                       WHERE budget_name = ? AND topic = ?""",
                       (amount, budget_name, topic))
        self._connection.commit()

    def get_topics(self, budget_name):
        print(budget_name)
        cursor = self._connection.cursor()
        topics = cursor.execute("""SELECT topic, amount
                       FROM topics
                       WHERE budget_name = ?;""",
                                (budget_name,)).fetchall()
        print(topics)
        return topics

    def delete(self):
        with open(self._file_path, "w") as file:
            file.write("")


budget_repository = BudgetRepository(
    BUDGET_FILE_PATH, get_database_connection())
