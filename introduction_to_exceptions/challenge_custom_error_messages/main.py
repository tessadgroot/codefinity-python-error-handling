def safe_divide(num1, num2):
    try:
        result = int(num1) / int(num2)
        print("Result:", result)
    except ValueError:
        print('Please enter valid integers.')
    except ZeroDivisionError:
        print('Cannot divide by zero.')
    # Your code here: add except blocks for ValueError and ZeroDivisionError


# Example function calls for debugging:
safe_divide('10', '2')
safe_divide('abc', '2')
safe_divide('5', '0')