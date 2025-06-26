import json
import os 
from expense import Expense

class ExpenseTracker:
    ID = 1
    FILE_NAME = "data.json"

    def __init__(self):
        self.expenses = dict()
        self.categories = set()
        self.load_data()

    def add_expense (self, title, amount, category, date, notes=None):
        try:
            expense = Expense(self.ID, title, amount, category, date, notes)
            self.expenses[self.ID] = expense
            self.ID += 1
            if category not in self.categories:
                self.categories.add(category)
            print("Expense Added Successfully!")
            self.save_data()     
        except:           
            print("Error in adding expense") 
    
    def view_expenses (self):        
        return sorted(self.expenses.values(), key=lambda e: e.date, reverse=True)
    
    def delete_expense (self, id):
        try:
            del self.expenses[id]            
            print("Expense Deleted Successfully!")
            self.save_data()
        except:
            print(f"Expense with ID {id} does not exist.")

    def edit_expense (self, id, attrib, val):
        try:            
            expense = self.expenses[id]
            
            if attrib == "Title":
                expense.title = val 
            elif attrib == "Amount":
                expense.amount = int(val)
            elif attrib == "Category":
                expense.category = val 
            elif attrib == "Date":
                expense.date = val
            elif attrib == "Notes":
                expense.notes = val 

            self.expenses[id] = expense 
            print("Expense Edited Successfully!")
            self.save_data()
        except:
            print(f"Expense with ID {id} does not exist.")

    def expense_summary (self):
        summary = dict()

        total = 0 
        for e in self.expenses.values():
            total += e.amount
        
        summary["total"] = total
        summary["category_breakdown"] = dict()

        for c in self.categories:
            categ_total = 0
            for e in self.expenses.values():
                if e.category == c:
                    categ_total += e.amount
            if categ_total != 0:
                summary["category_breakdown"][c] = categ_total
            else:
                continue

        return summary
