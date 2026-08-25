# 🐍 Python Conditional Statements & Basic Programs

This repository contains a collection of beginner-friendly **Python programs** created to practice fundamental programming concepts such as conditional statements, nested conditions, list operations, user input, membership operators, and basic validation logic.

The programs are designed to strengthen problem-solving skills and provide practical understanding of how Python `if`, `elif`, and `else` statements are used to build decision-making applications.

---

## 📌 Overview

The repository includes several small Python programs based on real-world scenarios and logical problems.

These programs demonstrate how to:

* Take input from the user
* Apply conditional logic
* Use nested `if-else` statements
* Validate user input
* Perform operations on lists
* Check membership using the `in` operator
* Work with numbers, strings, and lists
* Implement simple banking and ticket-booking logic
* Use formatted strings with f-strings

---

## 🛠️ Technologies Used

* **Programming Language:** Python 3
* **IDE/Editor:** VS Code
* **Version Control:** Git & GitHub

---

## 📂 Programs Included

### 1. Odd Number and Divisibility Check

Checks whether a given number is odd and, if it is odd, verifies whether it is divisible by `7`.

**Concepts Covered:**

* Modulus operator `%`
* `if-else`
* Nested conditions
* User input

---

### 2. List Operations

Accepts user input and verifies whether the entered data is a list. If it is a list, different operations can be performed based on the selected option.

**Operations include:**

* Remove the last element using `pop()`
* Clear all elements using `clear()`
* Validate the selected option

**Concepts Covered:**

* `isinstance()`
* Lists
* `pop()`
* `clear()`
* Conditional statements

---

### 3. Facebook Username and Password Validation

A simple authentication program that checks whether the entered username and password match the predefined credentials.

**Concepts Covered:**

* String comparison
* Nested `if-else`
* User authentication logic
* Input validation

---

### 4. Driving License Eligibility

Determines whether a person is eligible to drive based on their age and driving license status.

**Logic:**

```text
Age >= 18
    ↓
Check License
    ↓
Yes → Can Drive
No  → Get License

Age < 18
    ↓
Under Age
```

**Concepts Covered:**

* Nested conditions
* Comparison operators
* String validation

---

### 5. ATM Withdrawal System

Simulates a basic ATM withdrawal process.

The program:

1. Verifies the PIN.
2. Requests the withdrawal amount.
3. Checks whether sufficient balance is available.
4. Allows or rejects the withdrawal.

**Concepts Covered:**

* Nested `if-else`
* Comparison operators
* Arithmetic operations
* Banking logic simulation

---

### 6. Loan Eligibility Check

Checks whether a person is eligible for a loan based on:

* Age
* Salary

The applicant must be **21 years or older** and have a salary of **₹25,000 or above**.

**Concepts Covered:**

* Nested conditions
* Logical decision-making
* Comparison operators

---

### 7. BookMyShow Ticket Booking Simulation

A basic movie ticket booking program that allows the user to select:

* Theater
* Movie
* Ticket amount

The program validates the theater and movie selection before processing the ticket amount.

**Concepts Covered:**

* Lists
* Membership operator `in`
* Nested conditions
* User input
* f-strings
* Basic booking-system logic

---

## 🧠 Python Concepts Practiced

| Concept              | Usage                     |
| -------------------- | ------------------------- |
| `if`                 | Decision making           |
| `elif`               | Multiple conditions       |
| `else`               | Alternative execution     |
| Nested `if`          | Multiple-level validation |
| `%` operator         | Divisibility checking     |
| `isinstance()`       | Data type validation      |
| `in` operator        | Membership checking       |
| `pop()`              | Removing list elements    |
| `clear()`            | Clearing a list           |
| `eval()`             | Converting user input     |
| `int()`              | Integer input             |
| f-strings            | Formatted output          |
| Lists                | Storing multiple values   |
| Comparison operators | Input validation          |

---

## 📁 Suggested Repository Structure

```text
Python-Basic-Programs/
│
├── odd_divisible_by_7.py
├── list_operations.py
├── username_password_validation.py
├── driving_license_validation.py
├── atm_withdrawal.py
├── loan_eligibility.py
├── movie_ticket_booking.py
│
└── README.md
```

---

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your system.

Check the installed version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone <your-repository-url>
```

### 3. Open the Project

```bash
cd Python-Basic-Programs
```

### 4. Run a Program

For example:

```bash
python odd_divisible_by_7.py
```

---

## 💡 Learning Objectives

The main objective of this repository is to build a strong foundation in Python programming and improve logical problem-solving skills.

By completing these programs, I practiced converting simple real-world requirements into Python decision-making logic. These exercises also helped me understand how nested conditions and input validation can be used to create basic interactive applications.

---

## 🚀 Future Improvements

The programs can be further improved by:

* Replacing `eval()` with safer input-handling methods
* Adding functions for reusable logic
* Adding exception handling
* Creating menu-driven applications
* Improving input validation
* Using dictionaries for structured data
* Adding automated test cases
* Developing GUI versions of selected programs

---

## 👨‍💻 Author

**Pranay Vishwanath Jadhao**

B.E. Electronics & Telecommunication Engineering

**Skills:** Python | SQL | HTML | CSS | JavaScript | Git | GitHub

---

## ⭐ Repository Purpose

This repository is part of my **Python learning and programming practice journey**, focusing on building strong fundamentals before moving toward advanced Python, SQL, data analysis, and software development concepts.

If you find this repository useful, consider giving it a ⭐ on GitHub.


