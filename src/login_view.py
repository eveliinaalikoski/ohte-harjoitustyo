from tkinter import ttk, constants

class LoginView:
    def __init__(self, root, handle_login):
        self._root = root
        self._handle_login = handle_login
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()
    
    def _iniatialize(self):
        self._frame = ttk.Frame(master = self._root)

        self._iniatialize_username_field()
        self._iniatialize_password_field()
        login_button = ttk.Button(master = self._frame,
                                  text = "Login",
                                  command = self._login_handler)
        login_button.grid(padx = 5, pady = 5, sticky = constants.EW)

        # add error message

    def _initialize_username_field(self):
        username_label = ttk.Label(master = self._frame, text = "Username")
        self._username_entry = ttk.Entry(master = self._frame)
        username_label.grid(padx = 5, pady = 5, sticky = constants.W)
        self._username_entry.grid(padx = 5, pady = 5, sticky = constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master = self._frame, text = "Password")
        self._password_entry = ttk.Entry(master = self._frame)
        password_label.grid(padx = 5, pady = 5, sticky = constants.W)
        self._password_entry.grid(padx = 5, pady = 5, sticky = constants.EW)

