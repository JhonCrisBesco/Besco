class BankAccount:
    def __init__(bank, account_number, owner, balance=0):
        bank.account_number = account_number
        bank.owner = owner
        bank.balance = balance
    
    def deposit(bank):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                bank.balance += amount
                print(f"Deposited ₱{amount}\nNew balance: ₱{bank.balance}")
            else:
                print("Can't deposit")
        except ValueError:
            print("Enter a valid number.")

    def withdraw(bank):
        try:
            amount = float(input("Enter amount to withdraw: "))
            print(f"Balance before withdraw: ₱{bank.balance}")
            if amount > 0 and amount <= bank.balance:
                bank.balance -= amount
                print(f"Withdrew ₱{amount}\nNew balance: ₱{bank.balance}")
            elif amount > bank.balance:
                print("Walang monar.")
            else:
                print("Can't withdraw.")
        except ValueError:
            print("Enter a valid number.")

    def display_balance(bank):
        print(f"Acc number: {bank.account_number}")
        print(f"Owner: {bank.owner}")
        print(f"Current balance: ₱{bank.balance}")

account = BankAccount("1", "Jhon Cris Besco",0)
account.display_balance()

account.deposit()
account.withdraw()
