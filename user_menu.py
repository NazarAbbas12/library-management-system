from book import Book
from members import Member

class User:
    def __init__(self):
        while True:
            reply = input(
    "\n========= USER MENU =========\n"
    "What would you like to do?\n\n"
    "1 → Borrow a Book\n"
    "2 → Return a Book\n"
    "3 → View Available Books\n"
    "4 → Search for a Book\n"
    "5 → Log Out\n\n"
    "Enter your choice (1-5): "
).strip()

            

            if reply == '1':
                title = input("Enter Book name:").lower()
                author = input("Enter author name:").lower()

                Book.borrow_book(title, author)
            elif reply == '2':
                member_id=input("Enter member id:")
                id= input("Enter book id:")
                Member.return_book(member_id,id)
                Book.return_book(id)

            elif reply == '3':
              Book.available_book()
            
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


            elif reply == '5':
                print("\nLOGGED OUT!!!")
                break
            else:
                print("\nOops! That doesn’t seem right. Please choose a valid option!")

