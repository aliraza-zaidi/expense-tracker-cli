from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.prompt import Prompt, IntPrompt
from expense_tracker import ExpenseTracker


class ExpenseTrackerCLI:
    def __init__ (self):
        self.tracker = ExpenseTracker()
        self.console = Console()

    def display_expense_table (self):
        table = Table(title="Expense Tracker")

        table.add_column("Expense ID")
        table.add_column("Title")
        table.add_column("Amount")
        table.add_column("Category")
        table.add_column("Date")
        table.add_column("Notes")

        for e in self.tracker.view_expenses():
            table.add_row(str(e.id), e.title, str(e.amount), e.category, e.date.strftime("%Y-%m-%d"), e.notes)

        self.console.print(table)

    def display_summary_table (self):        
        summary = self.tracker.expense_summary()
        header = Markdown(f"# **Expense Summary**")                        
        self.console.print(header)

        total_spent = Markdown(f"## **Total Amount Spent is Rs. {summary["total"]}**")                        
        self.console.print(total_spent)

        table = Table(title="Expense Breakdown by Category")
        table.add_column("Category")
        table.add_column("Expense (Rs.)")

        for key, val in summary["category_breakdown"].items():
            table.add_row(key, str(val))
        
        self.console.print(table)

    def prompt_add_expense (self):
        title = Prompt.ask("Title")
        amount = IntPrompt.ask("Amount (Rs.)")
        category = Prompt.ask("Category")
        date = Prompt.ask("Date (YYYY-MM-DD)")
        notes = Prompt.ask("Notes (optional)")

        self.tracker.add_expense(title, amount, category, date, notes)
    
    def prompt_edit_expense (self):        
        id = Prompt.ask("Expense ID")

        while True:
            options = ["Title", "Amount", "Category", "Date", "Notes", "Return"]
            choice = Prompt.ask("Choose an attribute to edit: ", choices=options)
            if choice == "Return":
                break
            value = Prompt.ask("Updated Value")
            self.tracker.edit_expense(int(id), choice, value)

    def prompt_delete_expense (self):
        id = Prompt.ask("Expense ID")
        self.tracker.delete_expense(int(id))

    def start_app (self):
        
        welcome = Markdown("# **Welcome to Expense Tracker Application!**")                        
        self.console.print(welcome)
        
        while True:
            options = ["View All", "Add", "Edit", "Delete", "Summary", "Exit"]
            choice = Prompt.ask("Choose an option: ", choices=options)

            if choice == "Exit":
                bye = Markdown("# **Bye and See You Soon!**")                        
                self.console.print(bye)
                break
            elif choice == "View All":
                self.display_expense_table()
            elif choice == "Summary":
                self.display_summary_table()
            elif choice == "Add":
                self.prompt_add_expense()
            elif choice == "Delete":
                self.prompt_delete_expense()
            else:
                self.prompt_edit_expense()

app = ExpenseTrackerCLI()
app.start_app()