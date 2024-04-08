from tkinter import ttk, constants

class BudgetView:
    def __init__(self, root, handle_logout):
        self.__root = root
        self._handle_logout = handle_logout
        self._window = None
        # self._user = 
        self._budget_window()
    
    def pack(self):
        self._window.pack(fill = constants.X)
    
    def destroy(self):
        self._window.destroy()
    
    def _budget_window(self):
        self._window = ttk.Frame(master = self._root)
        self._budget_list_frame = ttk.Frame(master = self._window)
        self._budget_list_frame.grid(row = 1, column = 0,
                                     columnspan = 2,
                                     sticky = (constants.EW))
        