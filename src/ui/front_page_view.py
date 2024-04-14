from tkinter import ttk, constants
from services.budget_service import budget_service
from entities.budget import Budget
from ui.budget_view import BudgetView

class BudgetListView:
    def __init__(self, root, budgets, front_page_view, show_budget_view):
        self._root = root
        self._budgets = budgets
        self._front_page_view = front_page_view
        self._show_budget_view = show_budget_view
        self._window = None
        self._budget_view = None
        
        self._budget_window()

    def pack(self):
        self._window.pack(fill = constants.X)

    def destroy(self):
        self._window.destroy()

    def _budget_view_helper(self, budget_name):
        self._show_budget_view(budget_name)

    def _list_budgets(self, budget):
        self._list_frame = ttk.Frame(master = self._window)
        budget_button = ttk.Button(master = self._list_frame, 
                                   text = budget.name,
                                   command = lambda: self._budget_view_helper(budget.name))
        budget_button.grid(row = 8, column = 0, padx = 5, pady = 5,
                           sticky = constants.W)
        self._list_frame.grid_columnconfigure(0, weight = 1)
        self._list_frame.pack(fill = constants.X)

    def _budget_window(self):
        self._window = ttk.Frame(master = self._root)
        for budget in self._budgets:
            self._list_budgets(budget)
        self._window.grid_columnconfigure(0, weight = 1, minsize = 400)
            

class FrontPageView:
    def __init__(self, root, show_budget_view, handle_logout):
        self._root = root
        self._show_budget_view = show_budget_view
        self._handle_logout = handle_logout
        self._window = None
        self._budget_list_view = None

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
                          text = "BudgetBuddy",
                          font = ("Arial", 25))
        logout_button.grid(row = 0, column = 0,
                           padx = 5, pady = 5,
                           sticky = constants.W)
        label.grid(row = 2, column = 0,
                   padx = 5, pady = 5,
                   sticky = constants.EW)
    
    def _create_helper(self):
        name_entry = self._new_name.get()
        if name_entry:
            budget_service.create_budget(name_entry)
            self._budget_list()
            self._new_name.delete(0, constants.END)

    def _new_budget(self):
        self._new_name = ttk.Entry(master = self._window)
        new_button = ttk.Button(master = self._window,
                                   text = "Create new budget",
                                   command = self._create_helper)
        self._new_name.grid(row = 4, column = 0, 
                            padx = 5, pady = 5,
                            sticky = constants.EW)
        new_button.grid(row = 4, column = 1,
                           padx = 5, pady = 5,
                           sticky = constants.EW)

    def _budget_list(self):
        if self._budget_list_view:
            self._budget_list_view.destroy()
        budgets = budget_service.get_budgets()
        self._budget_list_view = BudgetListView(self._front_page_frame,
                                                budgets,
                                                self._front_page_view,
                                                self._show_budget_view)
        self._budget_list_view.pack()

    def _front_page_view(self):
        self._window = ttk.Frame(master = self._root)
        self._front_page_frame = ttk.Frame(master = self._window)
        self._label()
        self._new_budget()
        self._budget_list()
        self._front_page_frame.grid(row = 6, column = 0,
                                    columnspan = 2,
                                    sticky = constants.EW)
        self._window.grid_columnconfigure(0, weight = 1, minsize = 400)
        self._window.grid_columnconfigure(1, weight = 0)