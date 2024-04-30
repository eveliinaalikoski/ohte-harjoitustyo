# Architecture

## Structure

Package diagram of the code:

![Package diagram](./pakkauskaavio.png)

The program consists of four main parts/directories:
- package *ui* contains user interface
- package *services* contains app logic
- package *repositories* contains saving information
- package *entities* contains source of information

## User interface

User interface contains four views:
- login & registeration
- front page
- budget view
- logout

These views have been created as their own classes. UI-class is responsible for showing these views. User interface only calls methods from BudgetService class, so it has been seperated from repositories.

## App logic

App logic's data model is formed by classes User and Budget.
Class User portrays users and Budget portrays budgets consisting the name of the budget and the creator of the budget.

```mermaid
classDiagram
    Budget "*" --> "1" User

    class Budget{
    name
    username
    }

    class User{
    username
    password
    }
```

## Main functionality

### User login

User writes username and password, and then clicks the login button.

```mermaid
sequenceDiagram
    user ->> UI: click login button
    UI ->> BudgetService: login("berta", "berta123")
    BudgetService ->> UserRepository: find_by_username("berta")
    UserRepository -->> BudgetService: user
    BudgetService -->> UI: user
    UI -> UI: show_front_page()
```