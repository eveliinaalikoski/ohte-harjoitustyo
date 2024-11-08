from pathlib import Path
from entities.budget import Budget
from config import BUDGET_FILE_PATH
from database_connection import get_database_connection


class BudgetRepository:
    """class responsible for database functions about budgets"""

    def __init__(self, file_path, connection):
        """class constructor

        Args:
            file_path: path to the file information in written in
            connection: database connection-object
        """
        self._file_path = file_path
        self._connection = connection

    def get_all(self):
        """returns all budgets

        Returns:
            list: list of tuples where is budget name and username
        """
        return self._read()

    def find_by_username(self, username):
        """finds the budgets current user has created

        Args:
            username (str-string): username whose budgets are searched

        Returns:
            list: list of Budget-objects
        """
        budgets = self.get_all()
        own_budgets = []
        for row in budgets:
            budget_name = row[0]
            user = row[1]
            if username == user:
                own_budgets.append(Budget(budget_name, user))
        return own_budgets

    def get_by_budget_name(self, budget_name, username):
        """Returns all budget information by budgetname and username

        Args:
            budget_name: name of the searched budget
            username: name of user that is currently logged in

        Returns:
            list of all budget information from table budgets
        """
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
        with open(self._file_path, encoding="UTF-8") as file:
            for row in file:
                row = row.replace("\n", "")
                part = row.split(";")
                budget_list.append((part[0], part[1]))
        return budget_list

    def create_budget(self, budget):
        """saves budget to database

        Args:
            budget (Budget-object): Budget-object of budget wanted to save
        """
        self._add(budget)

    def check_budget_name(self, budget_name):
        budgets = self.get_all()
        for b in budgets:
            if budget_name == b[0]:
                return False
        return True

    def _add(self, budget):
        self._file_exists()
        name = budget.name
        username = budget.username
        with open(self._file_path, "a", encoding="UTF-8") as file:
            file.write((name)+";")
            file.write((username)+"\n")

        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO budgets
                       (name, username, income, rent, groceries, hobbies)
                       VALUES (?, ?, 0, 0, 0, 0)""",
                       (name, username))
        self._connection.commit()

    def update_budget(self, budget_name, username, income,
                      rent, groceries, hobbies):
        cursor = self._connection.cursor()
        cursor.execute("""UPDATE budgets
                       SET income = ?, rent = ?, groceries = ?, hobbies = ?
                       WHERE name = ? AND username = ?""",
                       (income, rent, groceries, hobbies, budget_name, username))
        self._connection.commit()

    def add_topic(self, budget_name, topic, amount):
        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO topics
                       (budget_name, topic, amount)
                       VALUES (?, ?, ?)""",
                       (budget_name, topic, amount))
        self._connection.commit()

    def get_topics(self, budget_name):
        cursor = self._connection.cursor()
        topics = cursor.execute("""SELECT topic, amount
                                FROM topics
                                WHERE budget_name = ?;""",
                                (budget_name,)).fetchall()
        return topics

    def delete(self):
        """deletes all budgets from database"""
        with open(self._file_path, "w", encoding="UTF-8") as file:
            file.write("")
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM budgets")
        cursor.execute("DELETE FROM topics")
        self._connection.commit()


budget_repository = BudgetRepository(
    BUDGET_FILE_PATH, get_database_connection())
