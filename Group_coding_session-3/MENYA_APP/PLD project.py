
""" 
Classes:
    one for BOOK:
        - id: str/id
        - title: str
        - pages: int
        - last page: int(remeber off by one)
    one for library:
        - collection of books: {id: Book()}
        - active book: variable collesp to id
"""


class Book():

    """ we initialise it with id, title, content and turn_page = 0 
    and will increase as the user reads the book"""
    
    def __init__(self, id, title, author, content): 
        self.id = id
        self.title = title
        self.author = author
        self.content = content
        self.turn_page = 0
        
    def display_page(self):
        
        # this define where the read() func starts off
        
        return self.content[self.last_page]
    
    def turn_page(self):
        
        # turning pages will increment last page by 1 and return new display
        
        self.last_page += 1
        return self.display_page()
    
    def __str__(self):
        
        #func to pront the book and its pages and author
        
        return f"The book {self.title} by {self.author} has {self.content} pages"
    
    
class Library:
    
    def __init__(self):
        self.collection = dict()
        self.active_book = None
        self.id_counter = 0
        
    def add_to_collection(self, title, content):
        new_book = Book(id, title, content)
        self.collection[new_book.id] = new_book
        self.id_counter += 1
        



import getpass

name = input('username: ')
password = getpass.getpass(prompt="Enter your password: ")

print('_' * 70)

print("\n")

print(f'Welcome {name}')
print("\n")

print('_' * 70)
print("\n")

print('(1) BEL')
print('(2) BSE')
print('(3) BIT')
print('(4) BGC')
print('(5) BCS')

choice = 'no'

while choice not in [1, 2, 3, 4, 5]:

    choice = int(input('choose your faculty: '))

print('\n')

print('_' * 70)

if choice == 1:
   pass
elif choice == 2:
    pass
elif choice == 3:
    pass
elif choice == 4:
    pass
elif choice == 5:
    pass


new_book = Book(1, 'BIBLE', 'Jesus', 200)
print(new_book.id)
print(new_book.title)
print(new_book.author)
print(new_book.content)

print(new_book)