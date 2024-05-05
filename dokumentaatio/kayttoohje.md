# Manual

Load the source code from the latest release.

## Configuration

File names used to save information, are in .env -file (located in the start directory). Files are created to data directory.

## Installation

Before starting the app, load the dependencies:

```bash
poetry install
```

Then run required base command:

```bash
poetry run invoke build
```

Now you can start the app with the command:

```bash
poetry run invoke start
```

## Login & registeration

The app opens to the login&registeration view. You can login by filling in your username and password, and then pressing the login button. You can create a user by filling the input fields and pressing register.

## Creating a new budget

When you are logged in, you are directed to the front page. There you can create a new budget by filling a budget name and pressing Create new budget -button. Your budgets will be shown below the input field.

## Viewing your budget

In the front page your budgets are listed as buttons. By pressing a button, you are directed to the budget page. In the budget page, you can fill your budget and add topics with amounts.