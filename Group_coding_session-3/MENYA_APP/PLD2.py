import pymysql

class Book:
    def _init_(self, id, title, author, content):
        self.id = id
        self.title = title
        self.author = author
        self.content = content
        self.last_page = 0
        
    def display_page(self):
        return ' '.join(self.content.split()[self.last_page:])
    
    def turn_page(self):
        self.last_page += 1
        return self.display_page()
    
    def _str_(self):
        return f"The book {self.title} by {self.author} has {len(self.content.split())} pages"

class Library:
    def _init_(self):
        self.collection = {}
        self.active_book = None
        
    def add_book(self, book):
        self.collection[book.id] = book
        
    def select_book(self, book_id):
        if book_id in self.collection:
            self.active_book = self.collection[book_id]
        else:
            print("Book not found in library.")
            
    def read_book(self):
        if self.active_book is None:
            print("No book selected.")
        else:
            while True:
                print("Current page:")
                print(self.active_book.display_page())
                choice = input("Turn page? (y/n) ")
                if choice.lower() == "y":
                    self.active_book.turn_page()
                else:
                    break
                    
    def save_page(self):
        if self.active_book is None:
            print("No book selected.")
        else:
            db = pymysql.connect(host="localhost", user="username", password="password", database="database_name")
            cursor = db.cursor()
            sql = "UPDATE books SET last_page = %s WHERE id = %s"
            val = (self.active_book.last_page, self.active_book.id)
            cursor.execute(sql, val)
            db.commit()
            db.close()
            print("Page saved.")

# Create library object
library = Library()

# Create book objects
book1 = Book(1, "Python Programming", "John Smith", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed aliquet ultricies orci, vitae dictum leo bibendum in.")
book2 = Book(2, "Data Science Essentials", "Jane Doe", "Vivamus tempor massa neque, in pretium mauris vestibulum eget. Aenean vel sem vitae enim faucibus congue.")
book3 = Book(3, "Machine Learning with Python", "Jack Johnson", "Pellentesque suscipit ipsum a libero maximus, at lobortis neque tincidunt. Etiam fringilla arcu vel velit maximus tincidunt.")

# Add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Select book to read
library.select_book(1)

# Read book
library.read_book()

# Save current page
library.save_page()