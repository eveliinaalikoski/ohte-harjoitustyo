from tkinter import ttk, constants
from services.budget_service import budget_service


class BudgetView:
    def __init__(self, root, budget_name, to_front_page):
        self._root = root
        self._budget_name = budget_name
        self._to_front_page = to_front_page
        self._user = budget_service.get_current_user()
        self._window = None

        self._budget_window()

    def pack(self):
        self._window.pack(fill=constants.X)

    def destroy(self):
        self._window.destroy()

    def _label(self):
        front_button = ttk.Button(master=self._budget_frame,
                                  text="To front page",
                                  command=self._to_front_page)
        label = ttk.Label(master=self._budget_frame,
                          text=self._budget_name,
                          font=("Arial", 25),
                          foreground="blue")
        front_button.grid(row=0, column=0,
                          padx=5, pady=5,
                          sticky=constants.W)
        label.grid(row=2, column=0,
                   padx=5, pady=5,
                   sticky=constants.EW)

    def _budget_info(self):
        budget = budget_service.get_budget_info(
            self._budget_name, self._user.username)
        expences = 0000  # do the sum!!
        print("äääää", budget, budget[0])

        self._income_expences_field(budget[2], expences)
        self._rent_field(budget[3])
        self._groceries_field(budget[4])
        self._transportation_field(budget[5])
        self._hobbies_field(budget[6])

    def _income_expences_field(self, income, expences):
        income_text = ttk.Label(master=self._budget_frame,
                                text="income:",
                                background="#8ac936")
        self._income_entry = ttk.Entry(master=self._budget_frame)
        self._income_entry.insert(0, income)
        income_text.grid(row=4, column=0,
                         padx=5, pady=5,
                         sticky=constants.EW)
        self._income_entry.grid(row=4, column=1,
                                padx=5, pady=5,
                                sticky=constants.EW)
        expences_text = ttk.Label(master=self._budget_frame,
                                  text="expences:",
                                  background="#ed8d12")
        self._expences_entry = ttk.Entry(master=self._budget_frame)
        self._expences_entry.insert(0, expences)
        expences_text.grid(row=6, column=0,
                           padx=5, pady=5,
                           sticky=constants.EW)
        self._expences_entry.grid(row=6, column=1,
                                  padx=5, pady=5,
                                  sticky=constants.EW)

    def _rent_field(self, rent):
        rent_text = ttk.Label(master=self._budget_frame,
                              text="   rent:")
        self._rent_entry = ttk.Entry(master=self._budget_frame)
        self._rent_entry.insert(0, rent)
        rent_text.grid(row=8, column=0,
                       padx=5, pady=5,
                       sticky=constants.EW)
        self._rent_entry.grid(row=8, column=1,
                              padx=5, pady=5,
                              sticky=constants.EW)

    def _groceries_field(self, groceries):
        groceries_text = ttk.Label(master=self._budget_frame,
                                   text="   groceries:")
        self._groceries_entry = ttk.Entry(master=self._budget_frame)
        self._groceries_entry.insert(0, groceries)
        groceries_text.grid(row=10, column=0,
                            padx=5, pady=5,
                            sticky=constants.EW)
        self._groceries_entry.grid(row=10, column=1,
                                   padx=5, pady=5,
                                   sticky=constants.EW)

    def _transportation_field(self, transportation):
        transportation_text = ttk.Label(master=self._budget_frame,
                                        text="   transportation:")
        self._transportation_entry = ttk.Entry(master=self._budget_frame)
        self._transportation_entry.insert(0, transportation)
        transportation_text.grid(row=12, column=0,
                                 padx=5, pady=5,
                                 sticky=constants.EW)
        self._transportation_entry.grid(row=12, column=1,
                                        padx=5, pady=5,
                                        sticky=constants.EW)

    def _hobbies_field(self, hobbies):
        hobbies_text = ttk.Label(master=self._budget_frame,
                                 text="   hobbies:")
        self._hobbies_entry = ttk.Entry(master=self._budget_frame)
        self._hobbies_entry.insert(0, hobbies)
        hobbies_text.grid(row=14, column=0,
                          padx=5, pady=5,
                          sticky=constants.EW)
        self._hobbies_entry.grid(row=14, column=1,
                                 padx=5, pady=5,
                                 sticky=constants.EW)

    # def update(self):
    #     income = self._income_entry.get()
    #     rent = self._rent_entry.get()
    #     groceries = self._groceries_entry.get()
    #     transportation = self._transportation_entry.get()
    #     hobbies = self._hobbies_entry.get()

    #     budget_service.update_budget(self._budget_name,
    #                                  income,
    #                                  rent,
    #                                  groceries,
    #                                  transportation,
    #                                  hobbies)

    def _budget_window(self):
        self._window = ttk.Frame(master=self._root)
        self._budget_frame = ttk.Frame(master=self._window)

        self._label()
        self._budget_info()
        # self._update() will be added laterr

        self._budget_frame.grid(row=4, column=0,
                                columnspan=2,
                                sticky=(constants.EW))
        self._root.grid_columnconfigure(0, weight=1, minsize=400)
        self._root.grid_columnconfigure(1, weight=0)
