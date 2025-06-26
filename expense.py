from datetime import datetime

class Expense:
    def __init__(self, id, title, amount, category, date, notes=None):
        self.id = id
        self.title = title
        self.amount = int(amount)
        self.category = category
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.notes = notes 

    def __str__ (self):
        return f"Expense ID: {self.id}\nTitle: {self.title}\nAmount: {self.amount}\nCategory: {self.category}\nDate: {self.date}\nNotes: {self.notes}"
