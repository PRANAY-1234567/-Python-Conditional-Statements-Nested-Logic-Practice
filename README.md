🐍 Python Conditional Statements & Nested Logic Practice 

A collection of beginner-level Python programming exercises focused on conditional statements, nested conditions, list operations, membership operators, user validation, and real-world decision-making scenarios.

This repository is designed to strengthen Python fundamentals through practical programs such as ATM withdrawal validation, loan eligibility, ticket booking, login validation, and data-type operations.

📌 Overview

The programs in this collection demonstrate how Python conditional logic can be used to solve common programming problems.

The main concepts covered are:

if, elif, and else
Nested if statements
Comparison operators
Logical conditions
Membership operator in
Lists and list methods
Data-type checking with isinstance()
User input
String comparison
Basic validation
Real-world decision-making logic
📂 Programs Included
Python-Conditional-Programs/
│
├── 01_odd_divisible_by_7.py
├── 02_list_operations.py
├── 03_facebook_login_validation.py
├── 04_driving_license_validation.py
├── 05_atm_withdrawal.py
├── 06_loan_eligibility.py
├── 07_bookmyshow_ticket_booking.py
│
└── README.md
1️⃣ Odd Number and Divisibility by 7
📌 Description

This program checks whether a given number is odd. If the number is odd, it further checks whether it is divisible by 7.

Logic
Enter Number
     │
     ▼
Is number odd?
 ┌───┴────┐
No       Yes
│         │
Even    Divisible by 7?
          │
       ┌──┴──┐
      Yes    No
       │      │
   Divisible  Not Divisible
Concepts Used
Modulus operator %
Nested if
Conditional statements
User input
2️⃣ List Operations
📌 Description

This program checks whether the entered data is a list. If it is a list, the user can select an operation.

The available operations are:

Option	Operation
1	Remove and display last element
2	Remove and display last element
3	Clear the complete list
Concepts Used
Lists
isinstance()
pop()
clear()
Nested conditions
User-selected options
Example
Enter the data type: [10,20,30]
Hey its List Data Type


Enter the option(1,2,3): 3
[]

Note: In the provided code, options 1 and 2 both call data.pop(), so they currently perform the same operation.

3️⃣ Facebook Username and Password Validation
📌 Description

This program demonstrates a basic login validation system.

The program first checks the username. If the username is valid, it then checks the password.

Validation Flow
Username
   │
   ▼
Is username valid?
 ┌─┴─┐
No  Yes
│    │
Invalid
     ▼
 Check Password
     │
   ┌─┴─┐
  Yes  No
   │    │
Valid  Invalid
Concepts Used
Nested if
String comparison
User authentication logic
Input handling
4️⃣ Driving License Validation
📌 Description

This program determines whether a person can drive based on their age and driving license status.

Rules
Condition	Result
Age below 18	Under Age
Age ≥ 18 + License = Yes	Can Drive
Age ≥ 18 + License = No	Get License
Concepts Used
Nested if
Comparison operators
String comparison
Decision-making
5️⃣ ATM Withdrawal Validation
📌 Description

This program simulates a basic ATM withdrawal process.

The program first verifies the PIN. If the PIN is correct, it asks for the withdrawal amount and checks whether sufficient balance is available.

Logic
Enter PIN
   │
   ▼
Correct PIN?
 ┌─┴──┐
No   Yes
│      │
Wrong  Enter Amount
Pin       │
          ▼
     Amount <= Balance?
       ┌──┴──┐
      Yes    No
       │      │
 Withdraw   Insufficient
 Money      Balance
Example
Enter the Pin: 1234
Pin is correct


Enter the withdrawal amount: 2000
Yes, Withdraw Money 2000
Concepts Used
Nested if
Integer input
Balance validation
Comparison operators
Basic ATM logic
Alternative Implementation

The collection also contains another approach where the user enters the account balance before entering the withdrawal amount.

if pin == 1234:
    balance = eval(input("Enter the total Balance"))
    amount = eval(input("Enter the amount"))


    if amount <= balance:
        print("withdraw Money done")
        print("Total balance is ", balance - amount)
    else:
        print("Insufficient balance")
else:
    print("wrong Pin number")
6️⃣ Loan Eligibility Check
📌 Description

This program determines whether a person is eligible for a loan based on age and salary.

Eligibility Criteria
Age must be 21 or above
Salary must be 25,000 or more
Decision Table
Age	Salary	Result
≥ 21	≥ 25,000	Loan Eligible
≥ 21	< 25,000	Salary is Too Low
< 21	Any	Age Not Eligible
Concepts Used
Nested if
Comparison operators
Multiple conditions
Decision-making
7️⃣ BookMyShow Ticket Booking Simulation
📌 Description

This program demonstrates a simplified movie-ticket booking system.

The user selects:

Theater
Movie
Ticket amount

The program validates each selection before proceeding to the next step.

Available Theaters
["PVR", "Inox", "cinipole"]
Available Movies
["RRR", "Spiderman", "Hulk", "Captain america"]
Ticket Prices
[200, 300, 400, 500]
Booking Flow
Select Theater
      │
      ▼
Valid Theater?
 ┌────┴────┐
No        Yes
│          │
Error    Select Movie
             │
             ▼
        Valid Movie?
          ┌──┴──┐
         No    Yes
         │      │
       Error   Enter Amount
                   │
                   ▼
             Validate Amount
Concepts Used
Lists
Membership operator in
Nested if
User input
String comparison
List indexing
Basic booking logic
🧠 Key Python Concepts
Conditional Statements

The programs extensively use:

if condition:
    # statement
elif condition:
    # statement
else:
    # statement
Nested Conditions

Nested conditions are used when one condition depends on another.

Example:

if age >= 18:
    if license == "Yes":
        print("Can drive")
    else:
        print("Get license")
else:
    print("Under age")
Modulus Operator

The % operator is used for divisibility checks.

num % 2 == 0

checks whether a number is even.

num % 7 == 0

checks whether a number is divisible by 7.

Type Checking

The isinstance() function is used to determine whether a value belongs to a particular data type.

isinstance(data, list)
Membership Operator

The in operator checks whether an element exists inside a collection.

if user in theater:
    print("Theater selected")
List Methods

The programs demonstrate commonly used list methods:

pop()

Removes and returns an element.

data.pop()
clear()

Removes all elements from a list.

data.clear()

▶️ How to Run
Step 1: Install Python

Verify Python installation:

python --version
Step 2: Clone the Repository
git clone <your-repository-url>
Step 3: Open the Project
cd Python-Conditional-Programs
Step 4: Run a Program

For example:

python 01_odd_divisible_by_7.py
🎯 Learning Objectives

After completing these exercises, you will have practical experience with:

Python conditional statements
Nested if statements
User input
Number validation
String validation
List operations
Type checking
Membership operators
Basic authentication logic
ATM transaction logic
Loan eligibility logic
Ticket-booking logic
Real-world decision-making programs
🔮 Future Improvements

The programs can be extended by adding:

Exception handling with try-except
Functions for reusable logic
Loops for repeated operations
Menu-driven interfaces
Input validation
Object-Oriented Programming
Tkinter GUI
Flask web interface
Database integration
Automated unit testing
📚 Technologies Used
Technology	Purpose
Python	Core programming language
Conditional Statements	Decision-making
Lists	Store collections of data
Functions	Reusable logic
String Operations	User validation
Exception Handling	Future input validation
👨‍💻 Author

Pranay Jadhao

B.E. Electronics & Telecommunication Engineering

Technical Interests: Python • Java • SQL • Flask • Firebase • Software Development

📄 License

This project is intended for educational and learning purposes.

You are free to use and modify the programs for practice and learning.

⭐ If this repository helped you learn Python, consider giving it a Star!
