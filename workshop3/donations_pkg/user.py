def login(database, username, password):
    if username in database:
        if database[username] == password:
            print(f"Welcome back: {username}")
            return username
        else:
            print("invalid password")
            return ""
    else:
        print("Invalid username")
        return ""

def register(database, username, password):
    if username.lower() in database:
        print("username already exists")
        return ""
    elif len(username) > 10:
        print("Username cannot be longer than 10 characters")
        return ""
    elif len(password) <= 4:
        print("Password needs to be longer than 5 characters, you pnoob")
        return ""
    else:
        print("Username has been registered")
        return username

