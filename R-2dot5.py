class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit, balance=0):
        """Create a new credit card instance.
        The initial balance is zero.
        customer: the name of the customer (e.g., John Bowman)
        bank: the name of the bank (e.g., California Savings)
        acnt: the account identifier (e.g., 5391 0375 9387 5309)
        limit: credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance 

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        
        if price < 0:
            raise ValueError("Charge amount cannot be negative.")

        if price + self._balance > self._limit:
            return False  # Cannot accept charge if it would exceed the limit
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        
        if amount < 0:
            raise ValueError("Payment amount cannot be negative.")
        
        self._balance -= amount

# Example usage:
# card = CreditCard("John Bowman", "California Savings", "5391 0375 9387 5309", 1000)

# Valid operations
# print(card.charge(200))    # True
# print(card.get_balance())  # 200

# card.make_payment(50)
# print(card.get_balance())  # 150

# Invalid operations (will raise exceptions)
# print(card.charge("200"))  # Raises TypeError
# card.make_payment("50")    # Raises TypeError
# card.make_payment(-50)     # Raises ValueError

if __name__ == "__main__":
#    wallet = []
#    wallet.append(CreditCard("John Bowman", "California Savings", "5391 0375 9387 5309", 2500))
#    wallet.append(CreditCard("John Bowman", "California Federal", "3485 0399 3395 1954", 3500))
#    wallet.append(CreditCard("John Bowman", "California Finance", "5391 0375 9387 5309", 5000))

    # Adjust the loop to ensure exactly one card exceeds its limit
#    for val in range(1, 25):
#        wallet[0].charge(val)           # Card 1 will reach its limit with these charges
#        wallet[1].charge(val * 2)       # Card 2 will not exceed its limit with these charges
#        wallet[2].charge(val * 3)       # Card 3 will also not exceed its limit with these charges

    # Print details and process payments
#    for c in range(3):
#        print("Customer =", wallet[c].get_customer())
#        print("Bank =", wallet[c].get_bank())
#        print("Account =", wallet[c].get_account())
#        print("Limit =", wallet[c].get_limit())
#        print("Balance =", wallet[c].get_balance())
#        while wallet[c].get_balance() > 0:
#            wallet[c].make_payment(100)
#            print("New balance =", wallet[c].get_balance())
#        print()


    # Four-parameter constructor (balance defaults to 0)
    card1 = CreditCard("John Bowman", "California Savings", "5391 0375 9387 5309", 2500)
    print("Card 1 Balance:", card1.get_balance())  # Should print 0

    # Five-parameter constructor (initial balance is set)
    card2 = CreditCard("Jane Doe", "National Bank", "1234 5678 9012 3456", 3000, 150)
    print("Card 2 Balance:", card2.get_balance())
