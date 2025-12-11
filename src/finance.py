def calculate_total(expenses):
    # summerar alla uppgifter
    total = 0
    for item in expenses:
        total += item['amount']
        return total

def add_expenses(expenses, description, amount, category):
    # lägg till ny utgift i listan
    new_expense = {
        "description": description,
        "amount": float(amount),
        "category": category 
    }
    expenses.append(new_expense)
    return expenses

