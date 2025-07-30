from book import Book
from members import Member

class Admin:
    def __init__(self):
        while True:
            reply = input(
    "\n========= ADMIN MENU =========\n"
    "What would you like to do today?\n\n"
    "1 → Add a New Book\n"
    "2 → Remove a Book\n"
    "3 → View All Books\n"
    "4 → Search for a Book\n"
    "5 → Register a New Member\n"
    "6 → View All Members\n"
    "7 → Log Out\n\n"
    "Enter your choice (1-7): "
).strip()


            Book.instantiate_from_csv()

            if reply == '1':
                bookTitle = input("Enter Book Title:").lower()
                author = input("Enter Author Name:").lower()
                id = input("Enter Book ID:")
                
                Book(bookTitle, author, id)
                print("\nBOOK ADDED SUCCESSFULLY!!")
                Book.save_to_csv()

            elif reply == '2':
                id = input("Enter Id of Book which you want to remove:")
                Book.remove_book(id)

            elif reply == '3':
                Book.instantiate_from_csv()
                print("=======BOOKS=======")
                for book in Book.all:
                    print(book.__repr__())
            
            elif reply == '4':
                while True:
                    print("\n=== SEARCH FOR A BOOK ===")
                    searchBook = input(
                        "How would you like to search?\n"
                        "1 → By Title\n"
                        "2 → By Author\n"
                        "3 → By ID\n"
                        "4 → Exit Search\n"
                        "Your choice: "
                    ).strip()

                    if searchBook == '1':
                        ans = input("\nType the *title* of the book: ").strip().lower()
                        Book.search_book(ans)
                    elif searchBook == '2':
                        ans = input("\nType the *author* of the book: ").strip().lower()
                        Book.search_book(ans)
                    elif searchBook == '3':
                        ans = input("\nEnter the *Book ID*: ").strip()
                        Book.search_book(ans)
                    elif searchBook == '4':
                        print("\nThanks for visiting the library search! See you again soon.\n")
                        break
                    else:
                        print("\n⚠️ Invalid option! Please choose 1, 2, 3, or 4.\n")

            elif reply=='5':
                member_name=input("\nEnter Member Name: ").strip().lower()
                Member(member_name)
            
            elif reply=='6':
                Member.view_all_members()
                
            elif reply == '7':
                print("Logged out!!")
                break
            else:
              print("\nOops! That doesn’t seem right. Please choose a valid option!")

