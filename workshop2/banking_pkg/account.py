def show_balance(balance):
    print(f"Current Balance: ${balance}")


def deposit(balance):
    amount = float(input("Enter Amount To Deposit: "))
    balance += amount
    return balance


def withdraw(balance):
    amount = float(input("Enter Amount To Withdraw: "))
    if(balance < amount):
        print(" You do not have enough money")
        return balance
    return(balance - amount)


def logout(name):
    print(f"Goodbye: {name}")


def validate_length():
    while True:
        name = input("Enter Name to register: ")
        if len(name) in range(1, 10):
            return name
        else:
            print("name cannont be longer than 10 characters")


def validate_pin():
    while True:
        pin = input("Enter Pin: ")
        if len(pin) == 4:
            return pin
        else:
            print("pin must be 4 numbers")
