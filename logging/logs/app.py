import logging

## logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"), 
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(
    "ArithmeticApp"
)

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a}+{b} = {result} ")
    return result

def Subtracting(a,b):
    result = a-b
    logger.debug(f"Subtracting {a}-{b} = {result}")
    return result

def Multiplying(a,b):
    result = a*b
    logger.debug(f"Multiplying {a}*{b} = {result}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"divide {a}/{b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Devision by zero error")
        return None


add(10,15)
Subtracting(15,10)
Multiplying(10,20)
divide(20,0)

