from ui.login_view import LoginView
from ui.logout_view import LogoutView
from ui.front_page_view import FrontPageView
from ui.budget_view import BudgetView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _handle_logout(self):
        self._show_logout_view()

    def _handle_login(self):
        self._show_login_view()

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(
            self._root,
            self._show_front_page)
        self._current_view.pack()

    def _show_logout_view(self):
        self._hide_current_view()
        self._current_view = LogoutView(
            self._root,
            self.start)
        self._current_view.pack()

    def _show_front_page(self):
        self._hide_current_view()
        self._current_view = FrontPageView(
            self._root,
            self._show_budget_view,
            self._handle_logout)
        self._current_view.pack()

    def _show_budget_view(self, budget_name):
        self._hide_current_view()
        self._current_view = BudgetView(
            self._root,
            budget_name,
            self._show_front_page)
        self._current_view.pack()
