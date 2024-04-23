# Architecture

## Structure

Package diagram of the code:

![Package diagram](./pakkauskaavio.png)

The program consists of four main parts/directories:
- package *ui* contains user interface
- package *services* contains app logic
- package *repositories* contains saving information
- package *entities* contains source of information

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