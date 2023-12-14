import logging

logging.basicConfig(filename='logs.log', format='%(asctime)s,%(name)s:%(levelname)s:%(message)s:%(process)s:%(lineno)s', level=logging.DEBUG)

logging.debug("This is the debug message")
logging.info("Module 2 is completed")
logging.warning("This is the warning message")
logging.error("This is the error message")
logging.critical("This is CRITCAL")






