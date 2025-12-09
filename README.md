# Mithuna_SpyydaTech_Assessment

This repository contains all six programs that I implemented as part of the SpyydaTech assessment.  
Each file solves one specific use case, and all the solutions are written in simple, clean, and readable Python.  
Below is my explanation of the logic I used for each program, along with instructions on how to run them.

## 1. Logic Explanation

Across these six tasks, my goal was to keep the code understandable and to use basic Python features rather than complex or advanced structures. Each program focuses on a different idea such as stacks, dictionaries, dynamic programming, and text processing. Here is how I approached each one:

### Balanced Brackets
For this problem, I used a stack to check if parentheses or brackets are balanced. I pushed every opening bracket onto the stack and popped it when a matching closing bracket appeared. If the order was wrong at any point, or if the stack wasn’t empty at the end, then the input was not balanced. This is a simple and common way to validate nested structures.

### Balanced Increasing Subsequence
To find the length of the longest increasing subsequence, I used a list called `dp` where each position stores the length of the subsequence ending at that index. For each number, I compared it with the earlier numbers and updated the length when the sequence could be extended. The final answer is just the maximum value in the list. This approach is easy to understand and works well for typical inputs.

### Calculator with History
The calculator supports +, -, *, and /. After each calculation, I stored the result inside a list so that the history of all previous results can be viewed. The `get_history()` function simply returns the stored results. This shows how to maintain state across multiple operations.

### Library Management
For the library system, I used a dictionary to store books with their titles as keys. When adding a book, I inserted it into the dictionary. When removing one, I deleted the key. Returning the full list of books simply prints the dictionary. This task represents a basic CRUD-style system.

### URL Shortener
The URL shortener creates a random 6-character code for any URL entered. I used letters and digits to form the code and stored the mapping in a dictionary, so when someone enters the short code later, I can quickly return the original URL. This is a simplified version of how real URL shortener services work.

### Word Frequency Counter
The frequency counter splits a sentence into words and counts how many times each appears. I used a dictionary where the key is the word and the value is the count. This is a common idea used in many text-processing applications.

Across all tasks, I focused on readability and straightforward logic. Instead of optimizing heavily or complicating the programs, I tried to write them in a way that clearly shows the core concept behind each problem.

---

## 2. Files Overview

| File Name                         | Description |
|-----------------------------------|-------------|
| **balanced_brackets.py**          | Checks whether brackets are balanced using a stack. |
| **balanced_subsequence_length.py**| Finds the length of the longest increasing subsequence. |
| **calculator_with_history.py**    | Performs arithmetic operations and stores a history of results. |
| **library.py**                    | A simple library/book management system. |
| **url_shortener.py**              | Generates short codes for URLs and retrieves the original link. |
| **word_frequency.py**             | Counts how many times each word appears in a text. |

---

## 3. How to Run the Programs

### Step 1: Install Python
Make sure Python 3 is installed on your computer.

### Step 2: Clone the Repository
```bash
git clone https://github.com/Mithuna07/Mithuna_SpyydaTech_Assessment
cd Mithuna_SpyydaTech_Assessment
