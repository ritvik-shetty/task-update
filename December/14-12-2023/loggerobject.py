import logging
import sys
logging.basicConfig(filename='logobj.log', format='%(asctime)s,%(name)s:%(levelname)s:%(message)s:%(process)s:%(lineno)s')

logger=logging.getLogger("Ritvik")
# logger=logging.getLogger(sys.argv[0])
# logger=logging.getLogger(__name__)
logger.setLevel('DEBUG')
logger.info("Created the logger object")
logger.error("ERRROR")

