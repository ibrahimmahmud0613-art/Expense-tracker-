# expense_tracker.py

expenses = []
income = []

def add_income(amount, source):
    income.append({"amount": amount, "source": source})
    print(f"✅ Added income: {amount} from {source}")

def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})
    print(f"❌ Added expense: {amount} for {category}")

def show_summary():
    total_income = sum(item["amount"] for item in income)
    total_expenses = sum(item["amount"] for item in expenses)
    balance = total_income - total_expenses
    
    print("\n📊 --- Expense Tracker Summary --- 📊")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Balance: {balance}")
    print("-----------------------------------")

# Demo Run
if __name__ == "__main__":
    print("💰 Welcome to Expense Tracker 💰")
    add_income(5000, "Salary")
    add_income(200, "Freelance Job")
    add_expense(1000, "Food")
    add_expense(500, "Transport")
    show_summary()
