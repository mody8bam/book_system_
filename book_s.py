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
        # self.users={}
        # self.id=0
        

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
            
    # def adding_user(self,name):
    #     self.users[id]=name
    #     self.id+=1




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
        self.users={}
        self.user_id=0

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} to the library.")

    def list_book(self):
        for book in self.books:
            print(book)
    
    def add_user(self,name):
        self.users[self.user_id]=name
        print(f"Added user {name} with ID {self.user_id}")
        self.user_id+=1






def add_users_to_library(library,user):
    library.add_user(user)

def add_books_to_library(library,book):
    library.add_book(book)



# Main code block where conditions are evaluated
def main():
    library = Library()
    books = {}
    teachers = []
    students = []

    # Example user input to set the condition
    cond = int(input("Enter 1 to add a book, 2 to add a teacher, 3 to add a student: "))

    while True:
        print("\nOptions:")
        print("1: Add a Book")
        print("2: Add a Teacher")
        print("3: Add a Student")
        print("4: List Books")
        print("5: Exit")
        
        cond = int(input("Choose an option: "))

        match cond:
            case 1:
                bname = input("Enter Book name: ")
                btitle = input("Enter Title of book: ")
                books[bname] = btitle
                book = Book(bname, btitle)
                add_books_to_library(library, book)
            case 2:
                uname = input("Enter Teacher name: ")
                user = Teacher(uname)
                add_users_to_library(library, user)
            case 3:
                uname = input("Enter Student name: ")
                user = Student(uname)
                add_users_to_library(library, user)
            case 4:
                library.list_book()
            case 5:
                print("Exiting...")
                break
            case _:
                print("Invalid option. Please try again.")

# Function to add users to the library
def add_users_to_library(library, user):
    library.add_user(user.name)

# Function to add books to the library
def add_books_to_library(library, book):
    library.add_book(book)

# Run the main function
if __name__ == "__main__":
    main()
    
    
    
# library=Library()
# books={}
# teachers=[]
# students=[]

# match cond :
#     case 1:
#         bname=input(f"Enter Book name : ".title())
#         btitle=input(f"Enter Title of book : ".title())
#         books[bname]=btitle
#         book=Book(bname,btitle)
#         add_books_to_library(library,book)
#     case 2:
#         uname=input(f"Enter Teacher name : ")
#         user=Teacher(uname)
#         add_users_to_library(user)
#     case  3:
#         uname=input(f"Enter Student name : ")   
#         user=Student(uname)
#         add_users_to_library(user)
#     case _:
        


# #add books to library

# # def add_books2lib():
# book1=Book('1983','george orewll')
# book2 = Book("To Kill a Mockingbird", "Harper Lee")
# book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# #create users
# student = Student('mohammed')
# teacher=Teacher('Mr.smith')

# #list available books
# library.list_book()

# #borrow books
# student.borrow_book(book1, library)
# student.borrow_book(book2, library)
# teacher.borrow_book(book3, library)
# try :
#     student.borrow_book(book3, library)
# except :
#     print("something wrong")

