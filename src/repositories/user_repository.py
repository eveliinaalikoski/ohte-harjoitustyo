from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    """class responsible for database functions about users"""
    def __init__(self, connection):
        """class constructor

        Args:
            connection: database connection-object
        """
        self._connection = connection

    def get_all(self):
        """returns all users

        Returns:
            list: list of User-objects
        """
        cursor = self._connection.cursor()
        users = cursor.execute("SELECT * FROM users").fetchall()
        return users

    def create(self, user):
        """saves user's information to database
        
        Args:
            user: to be saved information as User-object
        
        Returns:
            user: saved User-object
        """
        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO users (username, password)
                       VALUES (?, ?)""", (user.username, user.password))
        self._connection.commit()
        return user

    def find_by_username(self, username):
        """Returns user with username
        
        Args:
            username: username of user that is returned

        Returns:
            User-object: if username exists
            None: if username doesn't exist
        """
        cursor = self._connection.cursor()
        row = cursor.execute("""SELECT * FROM users
                       WHERE username = ?""", [username]).fetchone()
        print(row)
        if not row:
            return None
        return User(row[0], row[1])

    def delete(self):
        """deletes all users from database"""
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
