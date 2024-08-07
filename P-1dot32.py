#def calculator():
#    """Simulate a simple calculator."""
#    import operator
#    
#    # Define operations
#    operations = {
#        '+': operator.add,
#        '-': operator.sub,
#        '*': operator.mul,
#        '/': operator.truediv
#    }
#    
#    current_value = None
#    current_op = None
#    
#    print("Simple Calculator")
#    print("Enter numbers and operators (+, -, *, /), and use '=' to get the result.")
#    
#    while True:
#        # Read input from user
#        user_input = input("Input: ").strip()
#        
#        # Exit the calculator
#        if user_input.lower() in ('quit', 'exit'):
#            print("Exiting calculator.")
#            break
#        
#        # Check if the input is a number
#        try:
#            num = float(user_input)
#            if current_value is None:
#                current_value = num
#            else:
#                if current_op is None:
#                    print("Error: No operator specified.")
#                else:
#                    current_value = current_op(current_value, num)
#                    current_op = None
#            print(f"Current value: {current_value}")
#        except ValueError:
#            # Handle input as an operator
#            if user_input in operations:
#                if current_op is not None:
#                    print("Error: Operator already set.")
#                else:
#                    current_op = operations[user_input]
#                    print(f"Operator set: {user_input}")
#            elif user_input == '=':
#                if current_value is None:
#                    print("Error: No result to display.")
#                else:
#                    print(f"Result: {current_value}")
#            else:
#                print("Error: Invalid input.")
#        
#        # Provide a line for clarity
#        print("-" * 20)
#
## Example usage
#calculator()

def print_help():
    print("Available commands:")
    print("  number        - Enter a number.")
    print("  +, -, *, /    - Perform arithmetic operations.")
    print("  =             - Calculate the result.")
    print("  C             - Clear the calculator.")
    print("  Q             - Quit the calculator.")
    print("  H             - Display this help message.")

class SimpleCalculator:
    def __init__(self):
        self.reset()

    def reset(self):
        self.current_value = 0
        self.current_operation = None
        self.is_new_operation = True

    def enter_number(self, number):
        if self.is_new_operation:
            self.current_value = number
            self.is_new_operation = False
        else:
            if self.current_operation is not None:
                if self.current_operation == '+':
                    self.current_value += number
                elif self.current_operation == '-':
                    self.current_value -= number
                elif self.current_operation == '*':
                    self.current_value *= number
                elif self.current_operation == '/':
                    if number == 0:
                        print("Error: Division by zero.")
                        return
                    self.current_value /= number
                self.current_operation = None
                self.is_new_operation = True
            else:
                print("Error: No operation to perform. Enter an operator first.")

    def set_operation(self, operation):
        if self.is_new_operation:
            print("Error: No number entered before operation.")
        else:
            self.current_operation = operation
            self.is_new_operation = False

    def calculate(self):
        if self.current_operation is not None:
            print("Error: Operation pending.")
        else:
            print(f"Result: {self.current_value}")
            self.reset()

def main():
    calc = SimpleCalculator()
    print("Welcome to the Simple Calculator!")
    print_help()

    while True:
        user_input = input("Enter command: ").strip().upper()
        if user_input == 'Q':
            print("Quitting calculator.")
            break
        elif user_input == 'C':
            calc.reset()
            print("Calculator cleared.")
        elif user_input == 'H':
            print_help()
        elif user_input in '+-*/':
            calc.set_operation(user_input)
        elif user_input == '=':
            calc.calculate()
        else:
            try:
                number = float(user_input)
                calc.enter_number(number)
            except ValueError:
                print("Invalid input. Please enter a number or a valid command.")

if __name__ == "__main__":
    main()

