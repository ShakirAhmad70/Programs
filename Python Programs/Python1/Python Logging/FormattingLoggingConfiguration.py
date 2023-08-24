import logging as log
# log.basicConfig(format="%(levelname)s") #No file name is passed, so output will be on consol
log.basicConfig(format="%(levelname)s : %(message)s") #No file name is passed, so output will be on consol

log.critical("This is critical msg")
log.error("This is error msg")
log.warning("This is warning msg")
log.info("This is info msg")
log.debug("This is debug msg")