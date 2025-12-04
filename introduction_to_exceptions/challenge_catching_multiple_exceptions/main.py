def safe_divide_from_string(number_str, divisor):
    # Your code here
    try:
        return 100/int(number_str)
        
    except ValueError:
        return 'a ValueError occurred.'
    except ZeroDivisionError:
        return 'Cannot divide by zero.'
    pass

# Example calls for debugging
a = safe_divide_from_string("10", 5)
b = safe_divide_from_string("0", 5)
c = safe_divide_from_string("abc", 5)
print(a)
print(b)
print(c)