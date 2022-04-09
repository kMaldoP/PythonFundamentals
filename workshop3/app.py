from donations_pkg.homepage import *
from donations_pkg.user import *

database = {"admin":"password123"}
donations = []
authorized_user = ""

show_homepage()

if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print(f"Login as: , {authorized_user} ")
while True:
    user_input = input("Choose an option: ")
    if user_input == "1":
        username = input("enter your username: ").lower()
        password = input(" enter password: ")
        authorized_user = login(database, username, password)
    elif user_input == "2":
        username = input("What is your username? ")
        password = input("Enter password: ")
        authorized_user = register(database, username, password)
        if authorized_user != "":
            database[username] = password 
    elif user_input == "3":
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
    elif user_input == "4":
        show_donations(donations)
    elif user_input == "5":
        print("Goodbye")
        break
