from tkinter import ttk, constants, StringVar
from services.budget_service import budget_service


class BudgetView:
    """View responsible for showing budget view"""

    def __init__(self, root, budget_name, to_front_page):
        """class constructor, creates new budget view

        Args:
            root: Tkinter-element where the view is created
            budget_name (variable): name of the viewed budget
            to_front_page (value): called to see front page
        """
        self._root = root
        self._budget_name = budget_name
        self._to_front_page = to_front_page
        self._user = budget_service.get_current_user()
        self._window = None
        self._update_button = None
        self._more_frame = None
        self._error_variable = None
        self._error_label = None

        self._budget_window()

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
        front_button = ttk.Button(master=self._budget_frame,
                                  text="To front page",
                                  command=self._to_front_page)
        label = ttk.Label(master=self._budget_frame,
                          text=self._budget_name,
                          font=("Arial", 25),
                          foreground="#287ed7")
        front_button.grid(row=0, column=0,
                          padx=5, pady=5,
                          sticky=constants.W)
        label.grid(row=2, column=0,
                   padx=5, pady=5,
                   sticky=constants.EW)

    def _budget_info(self):
        budget = budget_service.get_budget_info(
            self._budget_name, self._user.username)
        expences = sum(budget[3:])
        topics = budget_service.get_topics(self._budget_name)
        for topic in topics:
            expences += topic[1]
        self._income_expences_field(budget[2], expences)
        self._rent_field(budget[3])
        self._groceries_field(budget[4])
        self._hobbies_field(budget[5])
        self._more_field(topics)
        self._total(budget[2], expences)

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
        value_text = ttk.Label(master=self._budget_frame,
                               text=expences,
                               background="#ed8d12")
        expences_text.grid(row=6, column=0,
                           padx=5, pady=5,
                           sticky=constants.EW)
        value_text.grid(row=6, column=1,
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

    def _more_field(self, more):
        self._row = 16
        for m in more:
            string = "   " + m[0] + ":"
            topic_text = ttk.Label(master=self._budget_frame,
                                   text=string)
            amount_text = ttk.Label(master=self._budget_frame, text=m[1])
            topic_text.grid(row=self._row, column=0,
                            padx=5, pady=5,
                            sticky=constants.EW)
            amount_text.grid(row=self._row, column=1,
                             padx=5, pady=5,
                             sticky=constants.EW)
            self._row += 2

    def _add_more(self):
        self._row += 2
        if self._more_frame:
            self._more_frame.destroy()
        self._more_frame = ttk.Frame(master=self._budget_frame)
        bg = ttk.Label(master=self._more_frame, background="#90bb92")
        add_topic_text = ttk.Label(
            master=self._more_frame, text="new topic:", background="#90bb92")
        self._topic_entry = ttk.Entry(master=self._more_frame)
        add_amount_text = ttk.Label(
            master=self._more_frame, text="amount:", background="#90bb92")
        self._amount_entry = ttk.Entry(master=self._more_frame)
        add_button = ttk.Button(master=self._more_frame,
                                text="Add",
                                command=self._add_helper)
        bg.grid(row=0, column=0, rowspan=8, columnspan=2,
                padx=5, pady=5, sticky=(constants.NS, constants.EW))
        add_topic_text.grid(row=2, column=0,
                            padx=5, pady=5,
                            sticky=constants.EW)
        add_amount_text.grid(row=2, column=1,
                             padx=5, pady=5,
                             sticky=constants.EW)
        self._topic_entry.grid(row=4, column=0,
                               padx=5, pady=5,
                               sticky=constants.EW)
        self._amount_entry.grid(row=4, column=1,
                                padx=5, pady=5,
                                sticky=constants.EW)
        add_button.grid(row=6, column=1,
                        padx=5, pady=5,
                        sticky=constants.W)
        self._more_frame.grid(row=self._row, column=0,
                              columnspan=2,
                              sticky=(constants.EW))

    def _add_helper(self):
        topic_entry = self._topic_entry.get()
        amount_entry = self._amount_entry.get()
        try:
            int(amount_entry)
        except ValueError:
            self._budget_info()
            self._updating_button()
            self._show_error("amount can contain only numbers")
            self._add_more()
            self._topic_entry.delete(0, constants.END)
            self._amount_entry.delete(0, constants.END)
            return
        self._hide_error()
        if topic_entry and amount_entry:
            budget_service.add_topic(
                self._budget_name, topic_entry, amount_entry)
            self._update()
            self._budget_info()
            self._updating_button()
            self._add_more()
            self._topic_entry.delete(0, constants.END)
            self._amount_entry.delete(0, constants.END)

    def _total(self, income, expences):
        money = income - expences
        total = "total:", money, "€"
        total_text = ttk.Label(master=self._budget_frame,
                               text=total, background="#287ed7")
        total_text.grid(row=self._row, column=1,
                        padx=5, pady=5,
                        sticky=constants.E)
        self._row += 2

    def _updating_button(self):
        if self._update_button:
            self._update_button.destroy()
        self._update_button = ttk.Button(master=self._budget_frame,
                                         text="Update",
                                         command=self._update)
        self._update_button.grid(row=self._row, column=0,
                                 padx=5, pady=5,
                                 sticky=constants.W)
        self._row += 2

    def _correct_values(self, amount):
        try:
            int(amount)
        except ValueError:
            amount = 0
        amount = amount if amount else 0
        return amount

    def _update(self):
        income = self._correct_values(self._income_entry.get())
        rent = self._correct_values(self._rent_entry.get())
        groceries = self._correct_values(self._groceries_entry.get())
        hobbies = self._correct_values(self._hobbies_entry.get())
        
        budget_service.update_budget(self._budget_name,
                                     self._user.username,
                                     income,
                                     rent,
                                     groceries,
                                     hobbies)
        self._budget_info()

    def _budget_window(self):
        self._window = ttk.Frame(master=self._root)
        self._budget_frame = ttk.Frame(master=self._window)

        self._label()
        self._budget_info()
        self._updating_button()
        self._add_more()

        self._error_variable = StringVar(self._window)
        self._error_label = ttk.Label(master=self._window,
                                      textvariable=self._error_variable,
                                      foreground="red")
        self._error_label.grid(row=self._row, padx=5, pady=5)

        self._budget_frame.grid(row=4, column=0,
                                columnspan=2,
                                sticky=(constants.EW))
        self._root.grid_columnconfigure(0, weight=1, minsize=600)
        self._root.grid_columnconfigure(1, weight=0)
