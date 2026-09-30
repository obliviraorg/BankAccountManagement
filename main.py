from bank_account import BankAccount


print("===================================")
print("     BANK ACCOUNT MANAGEMENT")
print("===================================")

try:
    account_number = input("Enter account number: ")

    initial_balance = float(input("Enter initial balance: "))

    if initial_balance < 0:
        raise ValueError("Initial balance cannot be negative.")

    account = BankAccount(account_number, initial_balance)

    print("\nAccount created successfully!")

    while True:

        print("\n----------- MENU -----------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Account Number")
        print("5. Transaction History")
        print("6. Exit")
        print("----------------------------")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)


            elif choice == "2":

                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)


            elif choice == "3":

                print("Current Balance: ₹", account.get_balance())


            elif choice == "4":

                print("Account Number:", account.get_account_number())


            elif choice == "5":

                print("\n------- TRANSACTION HISTORY -------")

                transactions = account.get_transactions()

                if len(transactions) == 0:
                    print("No transactions yet.")
                else:
                    for transaction in transactions:
                        print(transaction)


            elif choice == "6":

                print("\nThank you for using Bank Account Management!")
                break


            else:

                print("Invalid choice! Please select 1-6.")


        except ValueError as e:

            print("Error:", e)


except ValueError as e:

    print("Error:", e)