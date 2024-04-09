from entities.user import User
from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

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
        return row
        

user_repository = UserRepository(get_database_connection())