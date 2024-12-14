class Calculator:
    def _init_(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'addition':
            return self.a + self.b
        elif self.operation == 'subtraction':
            return self.a - self.b
        elif self.operation == 'multiplication':
            return self.a * self.b
        elif self.operation == 'division':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Error: Invalid operation. Please choose addition, subtraction, multiplication, or division."

# Example usage
def main():
    # Provide predefined inputs for environments where input() is not supported
    test_cases = [
        (10.5, 2.5, 'addition'),
        (15.0, 5.0, 'subtraction'),
        (3.0, 4.0, 'multiplication'),
        (20.0, 4.0, 'division'),
        (10.0, 0.0, 'division'),  # Division by zero case
    ]

    for a, b, operation in test_cases:
        calc = Calculator(a, b, operation)
        result = calc.calculate()
        print(f"Operation: {operation.capitalize()}, a: {a}, b: {b} -> Result: {result}")

if __name__ == "_main_":
    main()