from tkinter import ttk, constants

class FrontPageView:
    def __init__(self, root, show_budget_view, handle_logout):
        self._root = root
        self._show_budget_view = show_budget_view
        self._handle_logout = handle_logout
        self._window = None

        self._front_page_view()

    def pack(self):
        self._window.pack(fill = constants.X)
    
    def destroy(self):
        self._window.destroy()


    def _label(self):
        logout_button = ttk.Button(master = self._window,
                                   text = "Logout",
                                   command = self._handle_logout)
        label = ttk.Label(master = self._window,
                          text = "BudgetView",
                          font = ("Arial", 25))
        logout_button.grid(row = 0, column = 0,
                           padx = 5, pady = 5,
                           sticky = constants.W)
        label.grid(row = 2, column = 0,
                   padx = 5, pady = 5,
                   sticky = constants.EW)

    def _front_page_view(self):
        self._window = ttk.Frame(master = self._root)
        self._front_page_frame = ttk.Frame(master = self._window)
        self._label()
        self._window.grid_columnconfigure(0, weight = 1, minsize = 400)
