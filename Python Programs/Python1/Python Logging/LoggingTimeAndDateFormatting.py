import logging as log

#for 12 hour format -> %I
# log.basicConfig(format='%(asctime)s, %(levelname)s, lineNo: %(lineno)s', datefmt='%d/%m/%Y %I:%M:%S%p')
#for 24 hour format -> %H
log.basicConfig(format='%(asctime)s, %(levelname)s, lineNo: %(lineno)s', datefmt='%d/%m/%Y %H:%M:%S')

#Visit this link for more information
#https://docs.python.org/3/library/time.html#time.strftime


print("Compare these results with the previous program(LoggingTime.py)")
log.critical("This is critical msg")
log.error("This is error msg")
log.warning("This is warning msg")
log.info("This is info msg")
log.debug("This is debug msg")