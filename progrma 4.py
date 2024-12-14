def count_multiples(numbers):
    # Initialize a dictionary to store the count of multiples
    multiple_counts = {i: 0 for i in range(1, 10)}

    # Iterate over each number in the list
    for num in numbers:
        # Check for multiples of numbers 1 to 9
        for i in range(1, 10):
            if num % i == 0:
                multiple_counts[i] += 1

    return multiple_counts

# Input list
input_numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Compute the output
output = count_multiples(input_numbers)

# Print the output
print(output)