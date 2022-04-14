class Category:

  # constructor
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.balance = 0.0
  # display output of each transaction
  def __str__(self):
    title = f"{self.name.center(30, '*')}\n"
    body = ""
    for t in self.ledger:
      left_content = "{:<23}".format(t['description'])
      right_content = "{:>7.2f}".format(t['amount'])
      body += "{0}{1}\n".format(left_content[:23], right_content[:7])
    total = "Total: {:.2f}".format(self.balance)
    output = title + body + total 
    return output

  # deposit method
  def deposit(self, amount, desc = ""):
    self.ledger.append({
      "amount": amount,
      "description": desc 
    })
    self.balance += amount

  # check balance method
  def get_balance(self):
    return self.balance

  # Used in withdraw and transfer method
  def check_funds(self, amount):
    if amount > self.balance:
      return False  
    else:
      return True
  # withdraw method
  def withdraw(self, withdraw_amount, desc = ""):
    if self.check_funds(withdraw_amount):
      self.ledger.append({
      "amount": withdraw_amount * -1,
      "description": desc
      })
      self.balance -= withdraw_amount
      return True
    else :
      return False
  # transfer method
  def transfer(self, amount, Category):
    if self.withdraw(amount, desc = f"Transfer to {Category.name}"):
      Category.deposit(amount, desc = f"Transfer from {self.name}")
      return True
    else :
      return False

# create spend chart
def create_spend_chart(categories):
  # find amount spent for each category
  categories_amount = []
  for c in categories:
    withdrawal_amount = 0
    for t in c.ledger:
      # withdrawal
      if t["amount"] < 0 :
        withdrawal_amount+= abs(t["amount"])
    categories_amount.append(round(withdrawal_amount,2))

  total_spent = round(sum(categories_amount),2)
  percentage_spent = list(map(lambda amount : int((((amount / total_spent) * 10) // 1) * 10), categories_amount))

  header = "Percentage spent by category\n"
  chart = ""
  for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in percentage_spent:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"
  footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
  labels = list(map(lambda category: category.name, categories))
  max_length = max(map(lambda  label: len(label), labels))
  labels = list(map(lambda label: label.ljust(max_length), labels))
  for x in zip(*labels):
      footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"
  return (header + chart + footer).rstrip("\n")