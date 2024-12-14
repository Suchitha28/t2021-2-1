def generate_series(a):
    if a < 1:
        print("Input must be a positive integer.")
        return

    result = []
    for i in range(a):
        result.append(1 + 2 * i)  # Calculate the odd numbers sequentially

    print(", ".join(map(str, result)))  # Convert numbers to string and join with a comma

# Example Usage
# Replacing input() with a predefined value to avoid I/O error in restricted environments.
a = int(input("enter the number")) # Example predefined value
generate_series(a)