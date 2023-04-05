import mysql.connector
from mysql.connector import Error

class Book:
    ...
    # Existing code unchanged

class Library:

    def __init__(self, db_config):
        self.collection = dict()
        self.active_book = None
        self.id_counter = 0
        self.db_config = db_config
        self.connect_to_db()

    def connect_to_db(self):
        try:
            self.connection = mysql.connector.connect(**self.db_config)
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")

    def close_db_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")

    def add_to_collection(self, title, author, content):
        new_book = Book(self.id_counter, title, author, content)
        self.collection[new_book.id] = new_book
        self.id_counter += 1
        self.add_book_to_db(new_book)

    def add_book_to_db(self, book):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO books (id, title, author, content) VALUES (%s, %s, %s, %s)"
            data = (book.id, book.title, book.author, book.content)
            cursor.execute(query, data)
            self.connection.commit()
            print(f"Book '{book.title}' added to the library and database.")
        except Error as e:
            print(f"Error while adding book to database: {e}")

    # Add other methods for modifying and retrieving data from the database

def main():
    # Replace the following database configuration with your own
    db_config = {
        'user': 'your_user',
        'password': 'your_password',
        'host': 'your_host',
        'database': 'your_database',
    }

    library = Library(db_config)

    while True:
        print("\nWelcome to the library!")
        print("1. Add a book")
        # Add more options
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            content = input("Enter the book content: ")
            library.add_to_collection(title, author, content)
        # Add more actions for other options
        elif choice == "0":
            library.close_db_connection()
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
# ... existing code ...

class Library:
    ...
    # Existing code unchanged

    def get_book_from_db(self, book_id):
        try:
            cursor = self.connection.cursor()
            query = "SELECT id, title, author, content FROM books WHERE id = %s"
            cursor.execute(query, (book_id,))
            result = cursor.fetchone()
            if result:
                return Book(result[0], result[1], result[2], result[3])
            else:
                return None
        except Error as e:
            print(f"Error while getting book from database: {e}")

    def update_book_in_db(self, book_id, updated_book):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE books SET title = %s, author = %s, content = %s WHERE id = %s"
            data = (updated_book.title, updated_book.author, updated_book.content, book_id)
            cursor.execute(query, data)
            self.connection.commit()
            print(f"Book '{updated_book.title}' updated in the database.")
        except Error as e:
            print(f"Error while updating book in database: {e}")

    def delete_book_from_db(self, book_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM books WHERE id = %s"
            cursor.execute(query, (book_id,))
            self.connection.commit()
            print(f"Book with ID {book_id} deleted from the database.")
        except Error as e:
            print(f"Error while deleting book from database: {e}")

def main():
    # ... existing code ...

    while True:
        print("\nWelcome to the library!")
        print("1. Add a book")
        print("2. View a book")
        print("3. Update a book")
        print("4. Remove a book")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # ... existing code ...
        elif choice == "2":
            book_id = int(input("Enter the book ID: "))
            book = library.get_book_from_db(book_id)
            if book:
                print(book)
            else:
                print(f"No book found with ID {book_id}")
        elif choice == "3":
            book_id = int(input("Enter the book ID: "))
            title = input("Enter the new book title: ")
            author = input("Enter the new author's name: ")
            content = input("Enter the new book content: ")
            updated_book = Book(book_id, title, author, content)
            library.update_book_in_db(book_id, updated_book)
        elif choice == "4":
            book_id = int(input("Enter the book ID: "))
            library.delete_book_from_db(book_id)
        elif choice == "0":
            library.close_db_connection()
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()