from datetime import datetime, timedelta

# -------- BOOK CLASS --------
class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def display(self):
        print(f"ID: {self.book_id} | {self.title} by {self.author} | Available: {self.copies}")


# -------- USER CLASS --------
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.issued_books = {}

    def issue_book(self, book_id):
        issue_date = datetime.now()
        due_date = issue_date + timedelta(days=7)
        self.issued_books[book_id] = (issue_date, due_date)

    def return_book(self, book_id):
        return self.issued_books.pop(book_id, None)

    def view_books(self):
        if not self.issued_books:
            print("No books issued.")
        else:
            print("\n--- Issued Books ---")
            for book_id, (issue, due) in self.issued_books.items():
                print(f"{book_id} | Issued: {issue.date()} | Due: {due.date()}")


# -------- LIBRARY SYSTEM --------
class LibrarySystem:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.current_user = None

    # -------- ADMIN --------
    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        copies = int(input("Enter Copies: "))

        self.books[book_id] = Book(book_id, title, author, copies)
        print("✅ Book added successfully!")

    def remove_book(self):
        book_id = input("Enter Book ID to remove: ")
        if book_id in self.books:
            del self.books[book_id]
            print("✅ Book removed.")
        else:
            print("❌ Book not found.")

    # -------- USER --------
    def register(self):
        username = input("Enter username: ")
        if username in self.users:
            print("User already exists.")
            return
        password = input("Enter password: ")
        self.users[username] = User(username, password)
        print("✅ Registered successfully!")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        user = self.users.get(username)
        if user and user.password == password:
            self.current_user = user
            print(f"✅ Welcome {username}")
            self.user_menu()
        else:
            print("❌ Invalid credentials")

    # -------- BOOK OPERATIONS --------
    def view_books(self):
        print("\n--- Available Books ---")
        for book in self.books.values():
            book.display()

    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")
        book = self.books.get(book_id)

        if not book:
            print("❌ Book not found.")
        elif book.copies <= 0:
            print("❌ No copies available.")
        else:
            book.copies -= 1
            self.current_user.issue_book(book_id)
            print("✅ Book issued successfully!")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")
        record = self.current_user.return_book(book_id)

        if not record:
            print("❌ You didn't issue this book.")
            return

        issue_date, due_date = record
        return_date = datetime.now()

        # Fine calculation
        fine = 0
        if return_date > due_date:
            late_days = (return_date - due_date).days
            fine = late_days * 5  # ₹5 per day

        self.books[book_id].copies += 1

        print("✅ Book returned successfully!")
        if fine > 0:
            print(f"💸 Fine: ₹{fine}")

    # -------- MENU --------
    def user_menu(self):
        while True:
            print("\n===== USER MENU =====")
            print("1. View Books")
            print("2. Issue Book")
            print("3. Return Book")
            print("4. My Books")
            print("5. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                self.view_books()
            elif choice == "2":
                self.issue_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.current_user.view_books()
            elif choice == "5":
                print("Logged out.")
                break
            else:
                print("Invalid choice")


# -------- MAIN --------
library = LibrarySystem()

# Sample books (for testing)
library.books["B1"] = Book("B1", "Python Basics", "Guido", 3)
library.books["B2"] = Book("B2", "Data Structures", "Mark", 2)

while True:
    print("\n====== LIBRARY SYSTEM ======")
    print("1. Admin - Add Book")
    print("2. Admin - Remove Book")
    print("3. Register")
    print("4. Login")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.remove_book()
    elif choice == "3":
        library.register()
    elif choice == "4":
        library.login()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice")

