Expense Tracker App in Python
This is a simple command-line expense tracker app built in Python. It allows users to input their expenses, categorize them, and save them to a spreadsheet. Here are the features and their implementation details:
Features:
Getting user expenses:
The app prompts the user to enter their expense details, such as the amount, category, and date. This information is then stored in a Python object.
Saving expenses to a file:
The app provides an option to save the expense data to a CSV file. This is done by iterating over the list of expenses and writing each expense as a row in the CSV file using the csv module.
Summarizing all expenses:
The app can summarize all the expenses by category and display the total amount spent in each category. This is done by iterating over the list of expenses and keeping a running total for each category.
Grouping expenses by category:
The app can group expenses by category and display them in a user-friendly format. This is done by iterating over the list of expenses and creating a dictionary where the keys are the categories and the values are lists of expenses belonging to that category.
Tracking remaining budget:
The app allows users to input their budget and tracks their remaining budget as they input expenses. This is done by keeping a running total of the expenses and subtracting it from the budget.
Implementation:
The app is built using Python 3 and the csv module for file handling. It uses object-oriented programming principles to define an Expense class that encapsulates the expense details. The app uses command-line input/output for user interaction.
The app consists of a single Python file, expense_tracker.py, which contains the main function and the Expense class. The main function handles user input/output and creates instances of the Expense class to represent each expense. The Expense class contains methods for getting and setting the expense details, as well as methods for summarizing and grouping expenses.
The app uses the csv module to read and write CSV files. When the user chooses to save their expenses to a file, the app creates a new CSV file or appends to an existing one, depending on the user's choice. The app writes each expense as a row in the CSV file, with columns for the amount, category, and date.
The app uses a dictionary to track the remaining budget. The dictionary has a single key, 'budget', and a value that is the remaining budget. The app updates the remaining budget after each expense is entered by subtracting the expense amount from the budget.
