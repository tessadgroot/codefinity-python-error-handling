def safe_divide(a, b):
    # Your code here
    try:
        return a/b
    except ZeroDivisionError:
        return 'Cannot divide by zero.'
    pass

print(safe_divide(10,2))
print(safe_divide(2,0))