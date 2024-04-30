# Changelog

## Week 3

- user can register, login and logout
- logged in user goes to the front page (but only a label atm)
- ui bases made for viewing budget, but doesn't work yet
- base entities made for user and budget
- user repository that saves data
- budget service that answer for app logic
- tests started: user login

## Week 4

- new functionality to front page:
    - logout button
    - button to create new budget
    - list of user's budgets
- budget page made:
    - button to go back to the front page
    - list of budget topics (made to look like a form)
        - changing the values of topics doesn't do anything yet
- tests: BudgetService

## Week 5

- added error message to front page if budget name is taken
- budget categories can be updated
- user can add topics to budgets (can't update them yet)
- tests: BudgetService, BudgetRepository, UserRepository

## Week 6

- user can add topics and the amount (this can't be edited later)
- tests: BudgetService, BudgetRepository, UserRepository
