from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self._root = root
        
    def start(self):
        label = ttk.Label(master = self._root, 
                          text = "yeppers")
        login_button = ttk.Button(master = self._root,
                            text = "login")
        register_button = ttk.Button(master = self._root,
                                     text = "register")

        label.grid(row = 0, column = 0, columnspan = 2, 
                   sticky = constants.W,
                   padx = 5, pady = 5)
        login_button.grid(row = 2, column = 1, 
                          sticky = (constants.E, constants.W),
                          padx = 5, pady = 5)
        register_button.grid(row = 4, column = 1, 
                             sticky = (constants.E, constants.W),
                             padx = 5, pady = 5)

        self._root.grid_columnconfigure(1, weight = 1, minsize = 300)

    # def _show_login(self):
    #     self._view = LoginView()