def generate_series(a):
    # Ensure the input is valid (positive integer)
    if a < 1:
        return "Input must be a positive integer."

    # Generate the series
    result = []
    for i in range(1, a + 1, 2):  # Generate odd numbers starting from 1
        result.append(i)

    # Return the series as a comma-separated string
    return ', '.join(map(str, result))

# Input
a = int(input("Enter an integer: "))
output = generate_series(a)
print(output)