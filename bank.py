class BankAccount:
    def __init__(self, owner, balance):
        self.owner   = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.history.append(f"+ Rs.{amount}")
        print(f"Deposited Rs.{amount}. Balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Balance: Rs.{self.balance}")
        else:
            self.balance = self.balance - amount
            self.history.append(f"- Rs.{amount}")
            print(f"Withdrew Rs.{amount}. Balance: Rs.{self.balance}")

    def show_statement(self):
        print(f"\n--- {self.owner}'s Statement ---")
        for entry in self.history:
            print(f"  {entry}")
        print(f"Current Balance: Rs.{self.balance}")

acc1 = BankAccount("Riya", 10000)
acc2 = BankAccount("Ali",   5000)

acc1.deposit(3000)
acc1.withdraw(2000)
acc1.withdraw(15000)
acc1.show_statement()

acc2.deposit(1000)
acc2.show_statement()