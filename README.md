# 🏦 Bank Account Management System

A simple **Bank Account Management System** developed in Python using Object-Oriented Programming (OOP).

## 📌 Project Description

This project simulates basic banking operations such as depositing money, withdrawing money, checking the account balance, and viewing transaction history.

The project uses **private attributes** to demonstrate encapsulation and **exception handling** to prevent invalid transactions and overdrafts.

## ✨ Features

* Create a bank account
* Store account number securely
* Set an initial balance
* Deposit money
* Withdraw money
* Check current balance
* View account number
* View transaction history
* Prevent negative or zero-value transactions
* Prevent overdrafts
* Handle invalid inputs using exceptions
* Menu-driven interface

## 🛠️ Technologies Used

* **Python 3**
* Object-Oriented Programming (OOP)
* Exception Handling
* Encapsulation

## 📂 Project Structure

```text
BankAccountManagement/
│
├── main.py
├── bank_account.py
└── README.md
```

### `bank_account.py`

Contains the `BankAccount` class and its methods:

* `deposit()`
* `withdraw()`
* `get_balance()`
* `get_account_number()`
* `get_transactions()`

### `main.py`

Contains the main program and menu-driven user interface.

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check the Python version using:

```bash
python --version
```

### 2. Open the project in VS Code

Open the `BankAccountManagement` folder in VS Code.

### 3. Open the terminal

Go to:

```text
Terminal → New Terminal
```

### 4. Run the program

```bash
python main.py
```

## 📋 Menu Options

```text
----------- MENU -----------
1. Deposit
2. Withdraw
3. Check Balance
4. Account Number
5. Transaction History
6. Exit
----------------------------
```

## ⚠️ Exception Handling

The program handles several invalid situations:

* Negative initial balance
* Zero or negative deposit
* Zero or negative withdrawal
* Withdrawal greater than available balance
* Invalid menu choices
* Invalid numerical input

For example, if the balance is ₹5000 and the user tries to withdraw ₹7000:

```text
Error: Insufficient balance! Overdraft not allowed.
```

## 💡 OOP Concepts Demonstrated

### Class

The `BankAccount` class represents a bank account.

### Object

An object of the class represents an individual bank account.

### Encapsulation

Account number, balance, and transaction history are stored as private attributes.

```python
self.__account_number
self.__balance
self.__transactions
```

### Methods

Different banking operations are implemented using methods such as:

```python
deposit()
withdraw()
get_balance()
```

### Exception Handling

`try-except` blocks are used to handle invalid inputs and transaction errors.

## 🔮 Future Improvements

The project can be extended with:

* Multiple bank accounts
* PIN-based login
* Account creation and deletion
* Transfer between accounts
* Interest calculation
* Saving data in a file or database
* Graphical User Interface (GUI)
* Detailed transaction timestamps

## 👨‍💻 Author

**Agnibesh Maity**

Python OOP Mini Project — Bank Account Management System
