from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE if exists users;")
    cursor.execute("DROP TABLE if exists budgets;")
    connection.commit()

def create_user_table(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE users
                   (id PRIMARY KEY,
                   username TEXT UNIQUE,
                   password TEXT);""")
    connection.commit()

def create_budget_table(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE budgets
                   (id PRIMARY KEY,
                   user_id INTEGER REFERENCES users);""")
    # add all the budget topics in tables?
    connection.commit()

def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_user_table(connection)
    create_budget_table(connection)

if __name__=="__main__":
    initialize_database()