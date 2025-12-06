
def process_numbers(numbers, divisor):
    # Output errors using print statements that start with 'ERROR:'
    for number in numbers:
        try:
            result = number / divisor
            print(f"Result: {result}")
        except Exception as e:
            # Print the error message in the format: ERROR: An error occurred: <exception message>
            print(f"ERROR: An error occurred: {e}")


# Example usage:
process_numbers([10, 20, 0, "a"], 0)
