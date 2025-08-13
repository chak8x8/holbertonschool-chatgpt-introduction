#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))


def get_amount(prompt):
    """
    Repeatedly prompt the user for a numeric, non-negative amount.
    Returns:
        float | None: The parsed amount, or None if the user cancels (Ctrl-D/Ctrl-C).
    """
    while True:
        try:
            raw = input(prompt)
        except (EOFError, KeyboardInterrupt):
            print("\nOperation cancelled.")
            return None

        try:
            amount = float(raw)
        except ValueError:
            print("Invalid amount. Please enter a number, e.g., 12.50")
            continue

        if amount < 0:
            print("Amount cannot be negative.")
            continue

        return amount


def main():
    cb = Checkbook()
    while True:
        try:
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if action == 'exit':
            break
        elif action == 'deposit':
            amount = get_amount("Enter the amount to deposit: $")
            if amount is not None:
                cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_amount("Enter the amount to withdraw: $")
            if amount is not None:
                cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
