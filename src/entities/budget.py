class Budget:
    """class that represents a budget"""
    def __init__(self, name=None, username=None):
        """class constructor, creates new budget

        Args:
            name (str, optional): 
                name of the created budget. Defaults to None.
            username (str, optional): 
                username of the user that created budget.
                Defaults to None.
        """
        self.name = name
        self.username = username