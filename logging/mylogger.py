import io
import logging
from datatime import datetime
import traceback
import types

class TimestampFormatter(logging.Formatter):
  def format(self, record):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{now}] {record.level}: {record.msg}"
    return message
def stack_trace(self, ex):
  buffer = io.stringIO()
  traceback.print_exception(type(ex), ex, ex.__traceback__, file=buffer)
  self.error(buffer.getvalue())

def get_logger(log_level):
  if 'my_logger' in logging.Logger.manager.loggerDict:
    return logging.getLogger('my_logger')
  else:
    logger = logging.getLogger('my_logger')
    logger.setLevel(log_level)
    handler = logging.FileHandler('application.log')
    handler.setFormatter(TimestampFormatter())
    logger.addHandler(handler)
    logger.stack_trace = types.MethodType(stack_trace, logger)
    return logger
