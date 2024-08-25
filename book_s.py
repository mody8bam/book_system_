##################################
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} - {'Borrowed' if self.is_borrowed else 'Available'}"

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
        return False

    def return_book(self):
        if self.is_barrowed:
            self.is_barrowed = False
            return True
        return False


##################################
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book, library):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else :
            print(f"{book.title} is already barrowed")
    def return_book(self,book,library):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else :
            print(f" {self.name} does not have {book.title} to return.")



##################################
class Student(User):
    def __init__(self, name):
        super().__init__(name)
        self.max_book=2

    def borrow_book(self, book, library):
        if len(self.borrowed_books) <self.max_book:
            super().borrow_book(book, library)
        else :
            print(f"{self.name} cannot barrow more than {self.max_book} books.")


##################################
class Teacher(User):
    def __init__(self, name):
        super().__init__(name)
        self.max_book=5
    def borrow_book(self,book,library):
        if len(self.borrowed_books) < self.max_book:
            super().borrow_book(book, library)
        else:
            print(f"{self.name} cannot borrow more than {self.max_book} books.")

##################################
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} to the library.")

    def list_book(self):
        for book in self.books:
            print(book)

library=Library()

#add books to library

# def add_books2lib():
book1=Book('1983','george orewll')
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

#create users
student = Student('mohammed')
teacher=Teacher('Mr.smith')

#list available books
library.list_book()

#borrow books
student.borrow_book(book1, library)
student.borrow_book(book2, library)
teacher.borrow_book(book3, library)
try :
    student.borrow_book(book3, library)
except :
    print("something wrong")

