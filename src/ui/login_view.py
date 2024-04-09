from tkinter import ttk, constants, StringVar
from services.budget_service import budget_service, InvalidCredentialsError, UsernameAlreadyExistsError

class LoginView:
    def __init__(self, root, handle_login):
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master = self._root)
        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(master = self._frame,
                                      textvariable = self._error_variable,
                                      foreground = "red")
        self._error_label.grid(padx = 5, pady = 5)

        self._initialize_username_field()
        self._initialize_password_field()

        login_button = ttk.Button(master = self._frame,
                                  text = "Login",
                                  command = self._login_handler)
        
        register_button = ttk.Button(master = self._frame,
                                  text = "Register",
                                  command = self._register_handler)
        
        self._frame.grid_columnconfigure(0, weight = 2, minsize = 400)
        login_button.grid(padx = 5, pady = 5, sticky = constants.W)
        register_button.grid(padx = 5, pady = 5, sticky = constants.E)        
        self._hide_error()

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

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        try:
            budget_service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error("Invalid username or password")
    
    def _register_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Username and password required")
            return
        
        try:
            budget_service.register(username, password)
            self._handle_login()
        except UsernameAlreadyExistsError:
            self._show_error("Username is already taken")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()
    
    def _hide_error(self):
        self._error_label.grid_remove()