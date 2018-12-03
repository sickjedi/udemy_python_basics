import psycopg2

connection_string = "dbname='bookstore_db' user='bookstore' password='bookstore' host='localhost' port='5432'"


def init_db():
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book ("
                   "id SERIAL PRIMARY KEY NOT NULL, "
                   "title TEXT, "
                   "author TEXT,"
                   "year INTEGER, "
                   "isbn INTEGER)")
    cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS book_id_uindex ON public.book (id)")
    connection.commit()
    connection.close()


def insert(title, author, year, isbn):
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO book(title, author, year, isbn) VALUES (%s, %s, %s, %s)", (title, author, year, isbn))
    connection.commit()
    connection.close()


def view():
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()
    connection.close()
    return rows


def search(title='', author='', year=None, isbn=None):
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    if year == '':
        year = None

    if isbn == '':
        isbn = None

    cursor.execute("SELECT * FROM book WHERE "
                   "title = %s OR "
                   "author = %s OR "
                   "year = %s OR "
                   "isbn = %s", (title, author, year, isbn))
    rows = cursor.fetchall()
    connection.close()
    return rows


def delete(id):
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM book WHERE id = %s", (id,))
    connection.commit()
    connection.close()


def update(id, title, author, year, isbn):
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("UPDATE book SET "
                   "title = %s, "
                   "author = %s, "
                   "year = %s, "
                   "isbn = %s "
                   "WHERE id = %s", (title, author, year, isbn, id))
    connection.commit()
    connection.close()