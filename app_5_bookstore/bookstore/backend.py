import psycopg2

connection_string = "dbname='bookstore_db' user='bookstore' password='bookstore' host='localhost' port='5432'"


class Database:

    def __init__(self):
        self.connection = psycopg2.connect(connection_string)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS book ("
                            "id SERIAL PRIMARY KEY NOT NULL, "
                            "title TEXT, "
                            "author TEXT,"
                            "year INTEGER, "
                            "isbn INTEGER)")
        self.cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS book_id_uindex ON public.book (id)")
        self.connection.commit()

    def insert(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO book(title, author, year, isbn) VALUES (%s, %s, %s, %s)",
                            (title, author, year, isbn))
        self.connection.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM book")
        rows = self.cursor.fetchall()
        return rows

    def search(self, title='', author='', year=None, isbn=None):
        if year == '':
            year = None

        if isbn == '':
            isbn = None

        self.cursor.execute("SELECT * FROM book WHERE "
                            "title = %s OR "
                            "author = %s OR "
                            "year = %s OR "
                            "isbn = %s", (title, author, year, isbn))
        rows = self.cursor.fetchall()
        return rows

    def delete(self, id):
        self.cursor.execute("DELETE FROM book WHERE id = %s", (id,))
        self.connection.commit()

    def update(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE book SET "
                            "title = %s, "
                            "author = %s, "
                            "year = %s, "
                            "isbn = %s "
                            "WHERE id = %s", (title, author, year, isbn, id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()