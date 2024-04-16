from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        cursor = self._connection.cursor()
        users = cursor.execute("SELECT * FROM users").fetchall()
        return users

    def create(self, user):
        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO users (username, password) 
                       VALUES (?, ?)""", (user.username, user.password))
        self._connection.commit()
        return user

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        row = cursor.execute("""SELECT * FROM users
                       WHERE username = ?""", [username]).fetchone()
        print(row)
        if not row:
            return None
        return User(row[0], row[1])
    
    def delete(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
