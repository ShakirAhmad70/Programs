import logging as log

log.basicConfig(filename='log.txt', level=log.DEBUG, filemode='w') #default level is WARNING(30) and default filemode is 'a'->append

print("This is the script to demonstrate the logging in python")

log.critical("This is critical message")
log.error("This is error message")
log.warning("This is warning message")
log.info("This is info message")
log.debug("This is debug message")