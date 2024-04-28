from tkinter import ttk, constants
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
        self._add_topic_text = None
        self._topic_entry = None
        self._add_amount_text = None
        self._amount_entry = None
        self._add_button = None

        self._budget_window()

    def pack(self):
        """shows window"""
        self._window.pack(fill=constants.X)

    def destroy(self):
        """destroys window"""
        self._window.destroy()

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
        if (self._add_topic_text or self._topic_entry or
            self._add_amount_text or self._amount_entry or
                self._add_button):
            self._add_topic_text.destroy()
            self._topic_entry.destroy()
            self._add_amount_text.destroy()
            self._amount_entry.destroy()
            self._add_button.destroy()

        self._add_topic_text = ttk.Label(
            master=self._budget_frame, text="new topic:")
        self._topic_entry = ttk.Entry(master=self._budget_frame)
        self._add_amount_text = ttk.Label(
            master=self._budget_frame, text="amount:")
        self._amount_entry = ttk.Entry(master=self._budget_frame)
        self._add_button = ttk.Button(master=self._budget_frame,
                                      text="Add",
                                      command=self._add_helper)
        self._add_topic_text.grid(row=self._row, column=0,
                                  padx=5, pady=5,
                                  sticky=constants.EW)
        self._add_amount_text.grid(row=self._row, column=1,
                                   padx=5, pady=5,
                                   sticky=constants.EW)
        self._row += 2
        self._topic_entry.grid(row=self._row, column=0,
                               padx=5, pady=5,
                               sticky=constants.EW)
        self._amount_entry.grid(row=self._row, column=1,
                                padx=5, pady=5,
                                sticky=constants.EW)
        self._row += 2
        self._add_button.grid(row=self._row, column=1,
                              padx=5, pady=5,
                              sticky=constants.W)

    def _add_helper(self):
        topic_entry = self._topic_entry.get()
        amount_entry = self._amount_entry.get()
        try:
            int(amount_entry)
        except ValueError:
            # add error message!!
            self._budget_info()
            self._updating_button()
            self._add_more()
            self._topic_entry.delete(0, constants.END)
            self._amount_entry.delete(0, constants.END)
            return

        if topic_entry and amount_entry:
            budget_service.add_topic(
                self._budget_name, topic_entry, amount_entry)
            self._budget_info()
            self._updating_button()
            self._add_more()
            self._topic_entry.delete(0, constants.END)
            self._amount_entry.delete(0, constants.END)

    def _total(self, income, expences):
        money = income - expences
        total = "total:", money
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

    def _update(self):
        income = self._income_entry.get()
        if not income:
            income = 0
        rent = self._rent_entry.get()
        if not rent:
            rent = 0
        groceries = self._groceries_entry.get()
        if not groceries:
            groceries = 0
        hobbies = self._hobbies_entry.get()
        if not hobbies:
            hobbies = 0
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

        self._budget_frame.grid(row=4, column=0,
                                columnspan=2,
                                sticky=(constants.EW))
        self._root.grid_columnconfigure(0, weight=1, minsize=600)
        self._root.grid_columnconfigure(1, weight=0)
