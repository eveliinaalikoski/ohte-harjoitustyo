from tkinter import ttk, constants, StringVar
from services.budget_service import budget_service


class BudgetListView:
    """View responsible for listing budgets"""

    def __init__(self, root, budgets, show_budget_view):
        """Class constructor, creates new list view for budgets

        Args:
            root: Tkinter-element where the view is created
            budgets (list): list of budgets
            show_budget_view (value): called to see budget view
        """
        self._root = root
        self._budgets = budgets
        self._show_budget_view = show_budget_view
        self._window = None
        self._budget_view = None

        self._budget_window()

    def pack(self):
        """shows window"""
        self._window.pack(fill=constants.X)

    def destroy(self):
        """destroys window"""
        self._window.destroy()

    def _budget_view_helper(self, budget_name):
        self._show_budget_view(budget_name)

    def _list_budgets(self, budget):
        self._list_frame = ttk.Frame(master=self._window)
        budget_button = ttk.Button(master=self._list_frame,
                                   text=budget.name,
                                   command=lambda: self._budget_view_helper(budget.name))
        budget_button.grid(row=8, column=0, padx=5, pady=5,
                           sticky=constants.W)
        self._list_frame.grid_columnconfigure(0, weight=1)
        self._list_frame.pack(fill=constants.X)

    def _budget_window(self):
        self._window = ttk.Frame(master=self._root)
        for budget in self._budgets:
            self._list_budgets(budget)
        self._window.grid_columnconfigure(0, weight=1, minsize=400)


class FrontPageView:
    """View responsible for showing front page"""

    def __init__(self, root, show_budget_view, handle_logout):
        """Class constructor, creates new front page view

        Args:
            root: Tkinter-element where the view is created
            show_budget_view (value): called to see budget view
            handle_logout (value): called when logging out
        """
        self._root = root
        self._show_budget_view = show_budget_view
        self._handle_logout = handle_logout
        self._window = None
        self._budget_list_view = None
        self._error_variable = None
        self._error_label = None
        self._user = budget_service.get_current_user()
        self._front_page_view()

    def pack(self):
        """shows window"""
        self._window.pack(fill=constants.X)

    def destroy(self):
        """destroys window"""
        self._window.destroy()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _label(self):
        logout_button = ttk.Button(master=self._window,
                                   text="Logout",
                                   command=self._handle_logout)
        label = ttk.Label(master=self._window,
                          text="BudgetBuddy",
                          font=("Arial", 25),
                          foreground="orange")
        logout_button.grid(row=0, column=0,
                           padx=5, pady=5,
                           sticky=constants.W)
        label.grid(row=2, column=0,
                   padx=5, pady=5,
                   sticky=constants.EW)

    def _create_helper(self):
        name_entry = self._new_name.get()
        if budget_service.check_budget_name(name_entry) == False:
            self._show_error("Budget name taken")
            return
        self._hide_error()
        if name_entry:
            budget_service.create_budget(name_entry)
            self._budget_list()
            self._new_name.delete(0, constants.END)

    def _new_budget(self):
        self._new_name = ttk.Entry(master=self._window)
        self._new_name.insert(0, "budget name")
        new_button = ttk.Button(master=self._window,
                                text="Create new budget",
                                command=self._create_helper)
        self._new_name.grid(row=6, column=0,
                            padx=5, pady=5,
                            sticky=constants.EW)
        new_button.grid(row=6, column=1,
                        padx=5, pady=5,
                        sticky=constants.EW)
        self._new_name.bind("<FocusIn>", self._name_delete)

    def _name_delete(self, e):
        self._new_name.delete(0, "end")

    def _budget_list(self):
        if self._budget_list_view:
            self._budget_list_view.destroy()
        budgets = budget_service.get_budgets()
        self._budget_list_view = BudgetListView(self._front_page_frame,
                                                budgets,
                                                self._show_budget_view)
        self._budget_list_view.pack()

    def _front_page_view(self):
        self._window = ttk.Frame(master=self._root)
        self._front_page_frame = ttk.Frame(master=self._window)

        self._error_variable = StringVar(self._window)
        self._error_label = ttk.Label(master=self._window,
                                      textvariable=self._error_variable,
                                      foreground="red")
        self._error_label.grid(row=4, padx=5, pady=5)

        self._label()
        self._new_budget()
        self._budget_list()

        self._front_page_frame.grid(row=8, column=0,
                                    columnspan=2,
                                    sticky=constants.EW)
        self._window.grid_columnconfigure(0, weight=1, minsize=400)
        self._window.grid_columnconfigure(1, weight=0)
        self._hide_error()
