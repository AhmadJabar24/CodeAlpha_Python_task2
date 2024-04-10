import tkinter as tk

class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

expenses = []

def add_expense():
    amount = float(amount_entry.get())
    category = category_entry.get()
    date = date_entry.get()
    expenses.append(Expense(amount, category, date))
    status_label.config(text="Expense added successfully!")

def show_summary():
    categories = {}
    for expense in expenses:
        if expense.category in categories:
            categories[expense.category] += expense.amount
        else:
            categories[expense.category] = expense.amount
    
    summary_text = "Expense Summary:\n"
    for category, total_amount in categories.items():
        summary_text += f"{category}: ${total_amount:.2f}\n"
    
    summary_label.config(text=summary_text)

# Create Tkinter window
window = tk.Tk()
window.title("Expense Tracker")



# Add Expense Section
amount_label = tk.Label(window, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()

category_label = tk.Label(window, text="Category:")
category_label.pack()
category_entry = tk.Entry(window)
category_entry.pack()

date_label = tk.Label(window, text="Date (YYYY-MM-DD):")
date_label.pack()
date_entry = tk.Entry(window)
date_entry.pack()

add_button = tk.Button(window, text="Add Expense", command=add_expense)
add_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

# Show Summary Section
summary_button = tk.Button(window, text="Show Summary", command=show_summary)
summary_button.pack()

summary_label = tk.Label(window, text="")
summary_label.pack()

window.mainloop()
