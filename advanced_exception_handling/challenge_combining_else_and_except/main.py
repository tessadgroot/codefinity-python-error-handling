def convert_and_report(s):
    # Your code here
    try:
        integer_s = int(s)
    except ValueError:
        print("Conversion failed: invalid integer")
    else:
        print(f"Conversion successful: {integer_s}")
    pass

convert_and_report('42')
convert_and_report('abc')
