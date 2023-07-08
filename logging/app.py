import logging
import mylogger

logger = mylogger.get_logger(log_level=logging.DEBUG)

try:
  logger.info("Application entered")
  x =  1 / 0
except Exception as e:
  logger.stack_trace(e)


logger.info("Application exiting")
