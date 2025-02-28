import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="main.log",
    format="[%(asctime)s.%(msecs)03d] %(levelname)-7s| %(process)06d >> %(thread)d | %(filename)s:%(lineno)d %(funcName)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)

def multiply(x, y):
    return x + y

def divide(x, y):
    return x / y

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return x ** (1 / 2)

if __name__ == "__main__":
    a = 4 - multiply(2,2)
    logger = logging.getLogger()
    logger.info(a)

