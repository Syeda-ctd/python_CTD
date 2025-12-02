import logging

# ---------- Logger Setup ----------
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


# ---------- Decorator ----------
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        # Prepare argument logging
        pos_args = args if args else "none"
        key_args = kwargs if kwargs else "none"

        # Call the original function
        result = func(*args, **kwargs)

        # Write to log
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {pos_args}")
        logger.log(logging.INFO, f"keyword parameters: {key_args}")
        logger.log(logging.INFO, f"return: {result}")
        logger.log(logging.INFO, "-" * 40)

        return result
    return wrapper


# ---------- Functions to Decorate ----------
@logger_decorator
def hello_world():
    print("Hello, World!")
    return None   # Explicit for logging


@logger_decorator
def many_positional(*args):
    return True


@logger_decorator
def many_keywords(**kwargs):
    return logger_decorator


# ---------- Mainline ----------
if __name__ == "__main__":
    hello_world()
    many_positional(10, 20, 30)
    many_keywords(a=1, b=2, c=3)
