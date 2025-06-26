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

    def serialize (self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "date": self.date.strftime("%Y-%m-%d"),
            "notes": self.notes,        
        }
    
    @staticmethod
    def deserialize (data):
        return Expense(data["id"], data["title"], data["amount"],
             data["category"], data["date"], data["notes"])