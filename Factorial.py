# Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage:
number = 5
factorial_result = factorial(number)
print(f"The factorial of {number} is: {factorial_result}")
