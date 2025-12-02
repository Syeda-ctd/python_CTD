# ---------- task2---------------------------
# Decorator that takes an argument
def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return type_of_output(result)  # convert the return value
        return wrapper
    return decorator


# ---------- Functions to Decorate ----------

@type_converter(str)
def return_int():
    return 5


@type_converter(int)
def return_string():
    return "not a number"


# ---------- Mainline ----------
if __name__ == "__main__":
    # Test return_int
    y = return_int()
    print(type(y).__name__)  # Should print "str"

    # Test return_string with error handling
    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!")  # Expected outcome
