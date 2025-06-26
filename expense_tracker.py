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