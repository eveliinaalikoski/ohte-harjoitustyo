from tkinter import ttk, constants
from services.budget_service import budget_service


class LogoutView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        budget_service.logout()
        self._handle_logout()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        text = ttk.Label(master=self._frame,
                         text="You have successfully logged out :)",
                         foreground="green",
                         font=("Arial", 15))
        back_to_login_button = ttk.Button(master=self._frame,
                                          text="Back to login!",
                                          command=self._logout_handler)
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        text.grid(padx=5, pady=5, sticky=constants.EW)
        back_to_login_button.grid(padx=5, pady=5, sticky=constants.EW)
