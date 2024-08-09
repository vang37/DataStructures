# Define the CreditCard class
class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self.customer = customer
        self.bank = bank
        self.account = acnt
        self.limit = limit
        self._balance = balance  # Use protected attribute

    def get_customer(self):
        return self.customer

    def get_bank(self):
        return self.bank

    def get_account(self):
        return self.account

    def get_limit(self):
        return self.limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self.limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        if amount < 0:
            raise ValueError("Payment amount must be positive.")
        self._balance -= amount

    def _set_balance(self, b):
        """Protected method to set balance, intended for subclass use."""
        if b < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = b

# Define the PredatoryCreditCard class extending CreditCard
class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr, balance=0):
        super().__init__(customer, bank, acnt, limit, balance)
        self.apr = apr
        self.charges_this_month = 0
        self.payment_made = False
        self.min_payment_percent = 0.02  # Minimum payment as a percentage of the balance
        self.late_fee = 25

    def charge(self, price):
        success = super().charge(price)
        if success:
            self.charges_this_month += 1
            if self.charges_this_month > 10:
                self._set_balance(self.get_balance() + 1)
        else:
            self._set_balance(self.get_balance() + 5)
        self.payment_made = False
        return success

    def make_payment(self, amount):
        super().make_payment(amount)
        self.payment_made = True

    def process_month(self):
        if self.get_balance() > 0:
            # Convert APR to a monthly multiplicative factor
            monthly_factor = pow(1 + self.apr, 1/12)
            new_balance = self.get_balance() * monthly_factor

            if not self.payment_made:
                min_payment = self.min_payment_percent * self.get_balance()
                if min_payment > self.get_balance():
                    new_balance += self.late_fee

            self._set_balance(new_balance)

        self.charges_this_month = 0
        self.payment_made = False

# Example usage
if __name__ == "__main__":
    # Create a PredatoryCreditCard instance
    card = PredatoryCreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500, 0.0825)

    # Simulate charges and payments
    for i in range(12):
        card.charge(100)

    # Simulate payment and process month
    card.make_payment(50)  # Payment less than the minimum required
    card.process_month()  # This will assess a late fee if required

    # Output results
    print("Balance after 12 charges, partial payment, and processing month:", card.get_balance())

