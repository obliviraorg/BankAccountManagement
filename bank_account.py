class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance
        self.__transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        self.__balance += amount
        self.__transactions.append(f"Deposited: ₹{amount}")
        print("Deposit successful!")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")

        if amount > self.__balance:
            raise ValueError("Insufficient balance! Overdraft not allowed.")

        self.__balance -= amount
        self.__transactions.append(f"Withdrawn: ₹{amount}")
        print("Withdrawal successful!")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_transactions(self):
        return self.__transactions