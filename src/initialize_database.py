from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE if exists users;")
    cursor.execute("DROP TABLE if exists budgets;")
    cursor.execute("DROP TABLE if exists topics;")
    connection.commit()


def create_user_table(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE users
                   (username TEXT UNIQUE,
                   password TEXT);""")
    connection.commit()


def create_budget_table(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE budgets
                   (name TEXT,
                   username TEXT REFERENCES users,
                   income INTEGER,
                   rent INTEGER,
                   groceries INTEGER,
                   transportation INTEGER,
                   hobbies INTEGER);""")
    # add all the budget topics in tables?
    connection.commit()

def create_topics_table(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE topics
                   (budget_name TEXT REFERENCES budgets,
                   topic TEXT,
                   amount INTEGER);""")
    connection.commit()

def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_user_table(connection)
    create_budget_table(connection)
    create_topics_table(connection)


if __name__ == "__main__":
    initialize_database()
