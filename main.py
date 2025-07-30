from admin_menu import Admin
from user_menu import User
while True:
    reply = input(
    "\n========= WELCOME TO THE LIBRARY =========\n"
    "Who are you logging in as?\n\n"
    "1 → Admin\n"
    "2 → User\n\n"
    "Enter your choice (1 or 2): "
).strip()

    if reply == '1':
        pass_word = input("Enter password:")
        if pass_word == "123":
            Admin()
            break
        else:
            print(f"Wrong Password!!")
            continue
    elif reply == '2':
        User()
        break
    else:
        print("Wrong Input!!")
