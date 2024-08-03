def check_arithmetic_formula(a, b, c):
    # Check the conditions
    if a + b == c:
        print(f"{a} + {b} = {c}")
    elif a == b - c:
        print(f"{a} = {b} - {c}")
    elif a * b == c:
        print(f"{a} * {b} = {c}")
    else:
        print("No valid arithmetic formula found.")

def main():
    # Input three integers from the user
    try:
        a = int(input("Enter the first integer (a): "))
        b = int(input("Enter the second integer (b): "))
        c = int(input("Enter the third integer (c): "))
    except ValueError:
        print("Please enter valid integers.")
        return

    # Check the arithmetic formulas
    check_arithmetic_formula(a, b, c)

if __name__ == "__main__":
    main()

