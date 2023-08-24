import logging as log

log.basicConfig(filename="logException.log", level=log.INFO, filemode='a', format="%(asctime)s, @line:%(lineno)s %(levelname)s:%(msg)s", datefmt="%d/%m/%Y %I:%M:%S %p")

log.info("A new request came")

try:
    x = int(input("Enter first Number: "))
    y = int(input("Enter Second Number: "))
    print("Division is: ", x/y)
except ZeroDivisionError as msg:
    print("Can't divide by zero")
    log.exception(msg)
except ValueError as msg:
    print("Please enter only int values")
    log.exception(msg)
finally:
    log.info("Request processing completed\n")