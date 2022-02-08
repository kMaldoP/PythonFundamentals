total_donations = 0

def show_homepage():
    print(""" 
      === DonateMe Homepage ===
    -------------------------------------
    | 1.    Login    | 2. Register       |
    | 3.    Donate   | 4. Show Donations |
    -------------------------------------
    |               5.  Exit             |
    -------------------------------------
    """)

def donate(username):
    global total_donations
    donation_amount = float(input("Enter amount to donate"))
    total_donations += donation_amount
    donation = (f"{username} donated ${donation_amount}")
    print("Thank you for your donation")
    return donation


def show_donations(donations):
    global total_donations
    print("\n--- All Donations ---")
    if len(donations) == 0:
        print(" Currently there are no donations, everyone is being cheap")
    else:
        for d in donations:
            print(d)
        print(f" Total Donations ${total_donations}")
