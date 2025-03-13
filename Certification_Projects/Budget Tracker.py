import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = self.name.center(30, "*") + '\n'
        items = ""
        for item in self.ledger:
            desc = item["description"]
            amount = "{:0.2f}".format(float(item["amount"]))
            if len(desc) > 23: desc = desc[0:23]
            if len(amount) > 7: amount = amount[0:7]
            items = items + desc + (30 - len(desc) - len(amount)) * " " + amount + '\n'

        return title + items + "Total: " + str(float(self.get_balance()))

    def deposit(self, amount, desc=''):
        self.ledger.append({'amount': amount, 'description': desc})

    def withdraw(self, amount, desc=''):
        if self.check_funds(amount):
            amount = amount * - 1
            self.ledger.append({'amount': amount, 'description': desc})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance = balance + entry['amount']
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to ' + category.name)
            category.deposit(amount, 'Transfer from ' + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False


def create_spend_chart(categories):
    totals = {}
    total = 0
    chart = "Percentage spent by category\n"
    for category in categories:
        totals[category.name] = 0
        for entry in category.ledger:
            if entry["amount"] < 0:
                totals[category.name] += entry["amount"]

    for k, v in totals.items():
        totals[k] = -v
        total -= v

    for k, v in totals.items():
        percentage = math.trunc((v / total * 100))
        totals[k] = percentage

    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "|"
        for v in totals.values():
            chart += " o " if v >= i else "   "
        chart += " \n"

    # Horizontal line: 4 spaces + 3*dashes per category + 1 extra dash
    chart += "    " + "-" * (3 * len(categories) + 1)

    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        chart += "\n    "
        for category in categories:
            if i < len(category.name):
                chart += " " + category.name[i] + " "
            else:
                chart += "   "
        chart += " "

    return chart


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))