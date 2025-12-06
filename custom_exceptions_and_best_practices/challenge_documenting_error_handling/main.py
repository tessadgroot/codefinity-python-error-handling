def read_first_line(content):
    """
    Returns the first line of the given string content.

    Exceptions:
        FileNotFoundError: Raised if the input is not a string.
        RuntimeError: Raised if any other error occurs while processing the input.

    The function attempts to treat the input as a string and returns the first line (up to the first newline character).
    If the input is not a string, it raises a FileNotFoundError.
    If any other exception occurs, it raises a RuntimeError with a message describing the original error.
    """

    try:
        if not isinstance(content, str):
            raise FileNotFoundError("Input is not a string.")
        lines = content.splitlines()        # this can be broken by the test harness
        return lines[0] if lines else ""
    except FileNotFoundError:
        raise
    except Exception as e:
        raise RuntimeError(f"Failed to read the first line: {e}")


# Example usage (for debug):
print(read_first_line('Hello World!\nSecond line'))
print(read_first_line("abc"))
