from tkinter import ttk, constants

class BudgetView:
    def __init__(self, root, budget_name, to_front_page):
        self._root = root
        self._budget_name = budget_name
        self._to_front_page = to_front_page
        self._window = None

        self._budget_window()
    
    def pack(self):
        self._window.pack(fill = constants.X)
    
    def destroy(self):
        self._window.destroy()
    
    def _label(self):
        front_button = ttk.Button(master = self._budget_frame,
                                   text = "To front page",
                                   command = self._to_front_page)
        label = ttk.Label(master = self._budget_frame,
                          text = self._budget_name,
                          font = ("Arial", 25),
                          foreground = "blue")
        front_button.grid(row = 0, column = 0,
                           padx = 5, pady = 5,
                           sticky = constants.W)
        label.grid(row = 2, column = 0,
                   padx = 5, pady = 5,
                   sticky = constants.EW)
    
    def _budget_info(self):
        text = ttk.Label(master = self._budget_frame,
                         text = "add info")
        text.grid(row = 4, column = 0,
                   padx = 5, pady = 5,
                   sticky = constants.EW)
    
    def _budget_window(self):
        self._window = ttk.Frame(master = self._root)
        self._budget_frame = ttk.Frame(master = self._window)
    
        self._label()
        self._budget_info()

        self._budget_frame.grid(row = 4, column = 0,
                                     columnspan = 2,
                                     sticky = (constants.EW))
        self._root.grid_columnconfigure(0, weight = 1, minsize = 400)
        self._root.grid_columnconfigure(1, weight = 0)