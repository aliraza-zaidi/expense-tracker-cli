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