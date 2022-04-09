


class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self):
        new_name = input("Enter a new username.")
        self.name = new_name
        return

    def change_pin(self):
        new_pin = input("Enter your new pin")
        self.pin = new_pin
        return


    def change_password(self):
        new_password = input("Enter your new password")
        self.password = new_password
        return

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(f" Your Account balance is: {self.balance}")

    def withdraw(self):
        amount = float(input("How much chedda do you need?"))
        self.balance -= amount
        return self.balance

    def deposit(self):
        amount = float(input("How much are you depositing?"))
        self.balance += amount
        return self.balance


    def transfer_money(self, user, amount):
        confirm_pin = int(input("confirm pin"))
        if confirm_pin == self.pin:
            user.balance += amount
            self.balance -= amount
            return True
        else:
            return False

    def request_money(self, user, amount):
        confirm_pin = int(input("confirm pin"))
        if confirm_pin == user.pin:
            confirm_password = input("Enter password")
            if confirm_password == self.password:
                user.balance -= amount
                self.balance += amount
                print(f"{self.name} now has a balance of: ${self.balance}")
                print(f"{user.name} has a balance of: ${user.balance}")
                return True
            return True
        else:
            return False



user1 = BankUser('bob', 1234, 'test')
user2 = BankUser('alice', 1234, 'test')

""""
code was tested using the python interactive terminal and dot notation. I believe it all to be functioning properly.
"""