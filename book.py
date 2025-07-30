import csv
from members import Member

class Book:
    all = []

    def __init__(self, title, author, ID, isBorrowed=False):
        self.__title = title
        self.__author = author
        self.__ID = ID
        self.__isBorrowed = isBorrowed == 'True' if isinstance(
            isBorrowed, str) else bool(isBorrowed)
        Book.all.append(self)

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def ID(self):
        return self.__ID

    @property
    def isBorrowed(self):
        return self.__isBorrowed

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        with open("books.csv", "r") as f:
            reader = csv.DictReader(f)
            for b in reader:
                Book(b['title'], b['author'], b['ID'], b['Is_Borrowed'])

    @classmethod
    def save_to_csv(cls):
        fieldnames = ["title", "author", "ID", "Is_Borrowed"]
        with open('books.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for book in Book.all:
                writer.writerow(book.to_dict())

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "ID": self.ID,
            "Is_Borrowed": self.isBorrowed
        }

    @classmethod
    def remove_book(cls, ID):
        for i in Book.all:
            if i.ID == ID:
                Book.all.remove(i)
                print(f"\nBook with ID:{ID} removed!!")

                with open('books.csv', 'r') as f:
                    reader = csv.DictReader(f)
                    books = [b for b in reader if b['ID'] != str(ID)]

                with open('books.csv', 'w', newline='') as f:
                    fieldnames = ['title', 'author', 'ID', 'Is_Borrowed']
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(books)
                break
        else:
            print(f"\nNo book found with ID:{ID}")

    @classmethod
    def search_book(cls, search):
        cls.instantiate_from_csv()

        found = False
        for book in cls.all:
            if search.lower() in book.title or search.lower() in book.author or search in book.ID:
                print(book)
                found = True
        if not found:
            print("\nNo book found!!")

    def __repr__(self):
        return f"Title: {self.__title}|Author: {self.__author}|ID: {self.__ID}|Borrowed: {self.__isBorrowed}"

# User menu methods
    @classmethod
    def borrow_book(cls, title, author):
        cls.instantiate_from_csv()

        for book in cls.all:
            if title in book.title and author in book.author:
                if book.isBorrowed == False:
                   
                    member_id=input("Enter your Member Id:")

                    Member.add_borrowed_book(member_id,book.ID)
                    print(f"\n{book.title} borrowed by you!!")
                    book._Book__isBorrowed = True
                    cls.save_to_csv()
                else:
                    print(f"\n{book.title} is already borrowed!!")
                break
        else:
            print(
                f"\nNo Book with title:{title} by author:{author} found!!")

    @classmethod
    def return_book(cls, bookID):
        # Load all books
        cls.instantiate_from_csv()
        rows = []
        found = False

        with open("books.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["ID"] == bookID:
                    found = True
                    if row.get("Is_Borrowed", "False") == "True":
                        row["Is_Borrowed"] = "False"
                        
                        print(f"Book ID {bookID} has been marked as returned.")
                    else:
                        print(f"Book ID {bookID} is already available.")
                rows.append(row)

        if found:
            # Save back to CSV
            with open("books.csv", "w", newline="") as f:
                fieldnames = ["title", "author", "ID", "Is_Borrowed"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            # Update in-memory book object
            for b in cls.all:
                if b.ID == bookID:
                    b._Book__isBorrowed = False
                    break
        else:
            print(f"No book with ID {bookID} found in the library.")


    @classmethod
    def available_book(cls):
        Book.instantiate_from_csv()
        print("===AVAILABLE BOOKS===")
        for book in Book.all:
            if not book.isBorrowed:
                print("\n", book)

        else:
            if not any(not book.isBorrowed for book in book.all):
                print("\nNO AVAILABLE BOOKS!")
