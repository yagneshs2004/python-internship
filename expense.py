import json
import os
from collections import defaultdict
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
DATA_FILE = "expense_data.json"
def load_expense_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return {"expenses": defaultdict(list)}
def save_expense_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=2)
def record_expense(data, amount, description, category, output_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if timestamp not in data["expenses"]:
        data["expenses"][timestamp] = []
    entry = {"timestamp": timestamp, "amount": amount, "description": description, "category": category}
    data["expenses"][timestamp].append(entry)
    save_expense_data(data)
    output_text.insert(tk.END, "Expense recorded successfully.\n")
def view_summary(data, year, output_text):
    selected_year_data = {timestamp: entries for timestamp, entries in data["expenses"].items() if timestamp.startswith(year)}
    if not selected_year_data:
        output_text.insert(tk.END, f"No expenses recorded for the year {year}.\n")
        return
    for timestamp, entries in selected_year_data.items():
        for entry in entries:
            output_text.insert(tk.END, f"Timestamp: {timestamp}\n")
            output_text.insert(tk.END, f"Category: {entry['category']}\n")
            output_text.insert(tk.END, f"Description: {entry['description']}\n")
            output_text.insert(tk.END, f"Amount: ₹{entry['amount']:.2f}\n")
            output_text.insert(tk.END, "-"*20 + "\n")
class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.data = load_expense_data()
        self.root.configure(bg="yellow")

        # Widgets
        self.menu_label = tk.Label(root, text="₹ EXPENSE TRACKER ₹", font=("Comic Sans MS", 16, "bold"), fg="black", bg="yellow")
        self.record_button = tk.Button(root, text=" Record an expense", command=self.record_expense_tab,font=("Helvetica", 12), fg="yellow", bg="black")
        self.view_summary_button = tk.Button(root, text=" View monthly summary", command=self.view_summary_tab,font=("Helvetica", 12), fg="yellow", bg="black")
        self.exit_button = tk.Button(root, text=" Exit", command=self.root.destroy,font=("Helvetica", 12), fg="yellow", bg="black")

        # Layout
        self.menu_label.grid(row=0, column=0, columnspan=5, pady=15)
        self.record_button.grid(row=1, column=0, columnspan=58, pady=10)
        self.view_summary_button.grid(row=2, column=0, columnspan=5, pady=15)
        self.exit_button.grid(row=3, column=0, columnspan=5, pady=10)

    def record_expense_tab(self):
        record_tab = tk.Toplevel(self.root)
        record_tab.title("Record Expense")
        record_tab.config(bg="yellow")

        # Widgets in record_tab
        amount_label = tk.Label(record_tab, text="Amount spent (₹):", font=("Helvetica", 12), fg="black", bg="yellow")
        amount_entry = tk.Entry(record_tab, font=("Helvetica", 12))
        description_label = tk.Label(record_tab, text="Description:", font=("Helvetica", 12), fg="black", bg="yellow")
        description_entry = tk.Entry(record_tab, font=("Helvetica", 12))
        category_label = tk.Label(record_tab, text="Category:", font=("Helvetica", 12), fg="black", bg="yellow")
        category_entry = tk.Entry(record_tab, font=("Helvetica", 12))
        output_text = tk.Text(record_tab, height=10, width=50, font=("Helvetica", 12))
        record_button = tk.Button(record_tab, text="Record Expense", command=lambda: record_expense(self.data, float(amount_entry.get()), description_entry.get(), category_entry.get(), output_text), font=("Helvetica", 12), fg="yellow", bg="black")
        back_button = tk.Button(record_tab, text="Back", command=record_tab.destroy, font=("Helvetica", 12), fg="yellow", bg="black")

        # Layout
        amount_label.grid(row=0, column=0, padx=10, pady=10)
        amount_entry.grid(row=0, column=1, padx=10, pady=10)
        description_label.grid(row=1, column=0, padx=10, pady=10)
        description_entry.grid(row=1, column=1, padx=10, pady=10)
        category_label.grid(row=2, column=0, padx=10, pady=10)
        category_entry.grid(row=2, column=1, padx=10, pady=10)
        output_text.grid(row=3, column=0, columnspan=2, pady=10)
        record_button.grid(row=4, column=0, pady=10)
        back_button.grid(row=4, column=1, pady=10)
    def view_summary_tab(self):
        summary_tab = tk.Toplevel(self.root)
        summary_tab.title("View Monthly Summary")
        summary_tab.config(bg="yellow")
        # Widgets
       # Widgets in summary_tab
        year_label = tk.Label(summary_tab, text="Enter the year (YYYY):", font=("Helvetica", 12), fg="black", bg="yellow")
        year_entry = tk.Entry(summary_tab, font=("Helvetica", 12))
        output_text = tk.Text(summary_tab, height=10, width=50, font=("Helvetica", 12))
        view_summary_button = tk.Button(summary_tab, text="View Summary", command=lambda: view_summary(self.data, year_entry.get(), output_text), font=("Helvetica", 12), fg="yellow", bg="black")
        back_button = tk.Button(summary_tab, text="Back", command=summary_tab.destroy, font=("Helvetica", 12), fg="yellow", bg="black")

        # Layout
        year_label.grid(row=0, column=0, padx=10, pady=10)
        year_entry.grid(row=0, column=1, padx=10, pady=10)
        output_text.grid(row=1, column=0, columnspan=2, pady=10)
        view_summary_button.grid(row=2, column=0, pady=10)
        back_button.grid(row=2, column=1, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()