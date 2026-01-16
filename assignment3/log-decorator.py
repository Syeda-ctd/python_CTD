import logging
import os

# One-time logging setup
log_path = os.path.join(os.path.dirname(__file__), "decorator.log")

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler(log_path, "a"))

# --- Decorator definition ---
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        # Function name
        func_name = func.__name__

        # Positional args
        positional = args if args else "none"
        # Keyword args
        keyword = kwargs if kwargs else "none"

        # Call the actual function
        result = func(*args, **kwargs)

        # Log everything
        logger.info(f"function: {func_name}")
        logger.info(f"positional parameters: {positional}")
        logger.info(f"keyword parameters: {keyword}")
        logger.info(f"return: {result}\n")

        return result
    return wrapper

# --- Functions using the decorator ---

@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def check_numbers(*args):
    return True

@logger_decorator
def show_info(**kwargs):
    return logger_decorator

# --- Mainline code ---
if __name__ == "__main__":
    say_hello()
    check_numbers(10, 20, 30)
    show_info(name="Syeda", country="USA")
