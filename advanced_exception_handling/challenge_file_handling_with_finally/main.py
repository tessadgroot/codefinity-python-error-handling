def read_file_contents(filename):
    # Your code here
    try:
        file = open(filename,'r')
        return file.read()
    except FileNotFoundError:
        file = None
        print('An error occurred while reading the file.')
        return None
    except Exception:
        file = None
        return 'An error occurred while reading the file.'
    finally:
        if file != None:
            file.close()
    pass

# Example usage for your testing:
with open('example.txt', 'w') as f:
    f.write('Hello, world!')
print(read_file_contents('example.txt'))
print(read_file_contents('nonexistent.txt'))
