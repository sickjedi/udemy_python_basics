import psycopg2

connection_string = "dbname='python_db' user='python' password='python' host='localhost' port='5432'"


def create_table():
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()


def insert(item, quantity, price):
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    connection.commit()
    connection.close()


def view():
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows


def delete(item):
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item = %s", (item,))
    connection.commit()
    connection.close()


def update_quantity(quantity, price, item):
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("UPDATE store set quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    connection.commit()
    connection.close()


# create_table()
# insert("Orange", 10, 15)
# delete('Orange')
update_quantity(11, 6, 'Apple')
print(view())
