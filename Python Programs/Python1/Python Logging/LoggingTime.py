import logging as log

log.basicConfig(format='%(asctime)s, %(levelname)s, lineNo: %(lineno)s')

log.critical("This is critical msg")
log.error("This is error msg")
log.warning("This is warning msg")
log.info("This is info msg")
log.debug("This is debug msg")