import csv
import os

class Member:
    all = []  # list of all Member objects in memory

    def __init__(self, name):
        self.__name = name
        self.__ID = Member.generate_new_id()  
        self.__borrowed_books = []  # empty list when created

        Member.all.append(self)
        self.save_to_csv()
        print(f"\nMember Registered Successfully!")
        print(f"Member ID: {self.__ID} | Name: {self.__name}")

    @property
    def name(self):
        return self.__name

    @property
    def ID(self):
        return self.__ID

    @property
    def borrowed_books(self):
        return self.__borrowed_books

   
    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        if not os.path.exists("members.csv"):
            return  # no file yet
        with open("members.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                 # Use a helper constructor to avoid creating a new ID
                member = cls.create_from_csv(
                    row["MemberID"],
                    row["MemberName"],
                    row["BorrowedBooks"]
                )
                cls.all.append(member)

    @classmethod
    def create_from_csv(cls, member_id, name, borrowed_books):
         # Create a "blank" Member object without triggering __init__
        obj = cls.__new__(cls)
        obj._Member__ID = int(member_id)
        obj._Member__name = name
        obj._Member__borrowed_books = [] if borrowed_books == "None" else borrowed_books.split(";")
        return obj

   
    @classmethod
    def add_borrowed_book(cls, member_id, bookID):
        cls.instantiate_from_csv()
        rows = []
        found = False

        with open("members.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["MemberID"] == member_id:
                    found = True
                    if row["BorrowedBooks"] == "None":
                        row["BorrowedBooks"] = bookID
                    else:
                        row["BorrowedBooks"] += ";" + bookID
                rows.append(row)

        if found:
            # Write back to CSV
            with open("members.csv", "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["MemberID", "MemberName", "BorrowedBooks"])
                writer.writeheader()
                writer.writerows(rows)

            # Update in-memory object
            for m in cls.all:
                if str(m.ID) == member_id:
                    m._Member__borrowed_books.append(bookID)
                    break

            print(f"Book {bookID} added to Member {member_id}'s borrowed list.")
        else:
            print(f"Member with ID {member_id} not found!")

   
    @classmethod
    def return_book(cls, member_id, bookID):
        cls.instantiate_from_csv()
        rows = []
        found = False
        updated = False

        with open("members.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["MemberID"] == member_id:
                    found = True
                    if row["BorrowedBooks"] != "None":
                        books = row["BorrowedBooks"].split(";")
                        if bookID in books:
                            books.remove(bookID)
                            row["BorrowedBooks"] = ";".join(books) if books else "None"
                            updated = True
                        else:
                            print(f"Book {bookID} is not borrowed by Member {member_id}")
                    else:
                        print(f"Member {member_id} has no borrowed books.")
                rows.append(row)  # Ensure it's always appended regardless

        if found and updated:
            # Write the updated data back to CSV
            with open("members.csv", "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["MemberID", "MemberName", "BorrowedBooks"])
                writer.writeheader()
                writer.writerows(rows)

            # Update in-memory object too
            for m in cls.all:
                if str(m.ID) == member_id and bookID in m._Member__borrowed_books:
                    m._Member__borrowed_books.remove(bookID)
                    break

            print(f"Book {bookID} returned by Member {member_id}.")
        elif not found:
            print(f"Member with ID {member_id} not found!")


            


    @staticmethod
    def generate_new_id():
        max_id = 0
        if os.path.exists('members.csv'):
            with open('members.csv', 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    max_id = max(max_id, int(row['MemberID']))
        return max_id + 1

   
    def save_to_csv(self):
        file_exists = os.path.exists('members.csv')
        fieldnames = ["MemberID", "MemberName", "BorrowedBooks"]

        with open("members.csv", 'a', newline='') as f:  # append mode
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()  # only once
            writer.writerow({
                "MemberID": self.__ID,
                "MemberName": self.__name,
                "BorrowedBooks": "None"
            })

   
    @classmethod
    def view_all_members(cls):
        Member.instantiate_from_csv()
        for member in Member.all:
            print(member)

    def to_dict(self):
        return {
            "MemberID": self.ID,
            "MemberName": self.name,
            "BorrowedBooks": ";".join(self.borrowed_books) if self.borrowed_books else "None"
        }

    def __repr__(self):
        borrowed = ";".join(self.__borrowed_books) if self.__borrowed_books else "None"
        return f"Member ID:{self.__ID}| Member Name:{self.__name}| Borrowed Books ID={borrowed})"
