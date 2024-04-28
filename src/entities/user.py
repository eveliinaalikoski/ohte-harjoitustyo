class User:
    """class that represents a user"""
    def __init__(self, username, password):
        """class constructor, creates new user

        Args:
            username (str-string): user's username
            password (str-string): user's password
        """
        self.username = username
        self.password = password
