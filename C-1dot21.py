def main():
    # Initialize an empty list to store the lines
    lines = []
    # Read lines from standard input
    print("Enter lines of text (Ctrl-D to end input):")
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass

    # Reverse the list of lines
    reversed_lines = lines[::-1]

    # Output the reversed lines
    print("\nReversed lines:")
    for line in reversed_lines:
        print(line)

if __name__ == "__main__":
    main()

