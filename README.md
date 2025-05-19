# Python Mini Projects 🐍

Mini Python projects created for practice, learning, and fun.  
Each project is self-contained and focuses on a specific concept or use case.  
This repository will continue to grow as I explore more areas in programming.

## 📁 Projects

### 🔐 Password Generator
A simple script that generates a random password based on the desired length.  
It includes uppercase and lowercase letters, digits, and punctuation characters.

#### 📌 How it works:
- The user is prompted to enter the desired password length.
- The script randomly selects characters and builds a password of that length.
- The result is printed to the screen.

#### ▶️ Example usage:
Input: Enter password length:  12
Output: The random password: X?QvE@Ynz7@R

#### 🛠 Technologies:
- Python standard library
  - `random`
  - `string`
 
    
### 🔎 Password Leak Checker

A script that checks if a password has ever been exposed in a data breach, using the **[Have I Been Pwned](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange)** API.

This tool demonstrates how to use hashing, API calls, and generators in Python.

#### 📌 How it works:
- The user enters a password.
- The password is hashed using the SHA1 algorithm.
- Only the first 5 characters of the hash are sent to the API (to preserve privacy).
- The API returns a list of leaked hash suffixes that match the prefix.
- The script checks if the full hash is among the leaked ones and tells the user how many times it appeared.

#### ▶️ Example usage:
Input: Enter a password to check: y7#Fw2p!aM0
Output: This password was NOT found. Good job!

#### 🛠 Technologies:
- Python standard library:
  - `hashlib` – for hashing the password with SHA1
  - `requests` – for sending HTTP requests to the API

---

### 💸 Bank Account

a script that simulates a basic banking system with basic functions such as checking and saving accounts, depositing and withdrawing money,  
setting interest rates for saving accounts, and keeping logs of all transactions.

## Purpose

The project is a simple practice exercise to Object-Oriented Programming (OOP) concepts in Python.  
It includes abstract classes, inheritance, encapsulation, and basic input validation.




