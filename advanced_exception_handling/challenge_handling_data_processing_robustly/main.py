def read_file_contents(filename):
    # Your code here
    try:
        file = open(filename,'r')
        print(file.read())
    except FileNotFoundError:
        print('Error: The file was not found.')
        file = None
        return file
    except UnicodeDecodeError:
        print('Error: Could not decode the file contents.')
        file = None
        return file
    finally:
         if file != None:
            file.close()
    pass


# Example calls for debug
def _create_test_files():
    # Create a valid file
    with open('example.txt', 'w') as f:
        f.write('Hello, world!')
    # Create a file with invalid utf-8 bytes
    with open('invalid.txt', 'wb') as f:
        f.write(b'\xff\xfe\xfd')

if __name__ == "__main__":
    _create_test_files()
    print("Valid file:")
    read_file_contents('example.txt')
    print("Nonexistent file:")
    read_file_contents('does_not_exist.txt')
    print("Invalid encoding file:")
    read_file_contents('invalid.txt')