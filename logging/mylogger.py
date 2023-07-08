import io
import logging
import traceback
import types
from datetime import datetime


class TimestampFormatter(logging.Formatter):
    def format(self, record):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"[{now}] {record.levelname}: {record.msg}"
        return message


def stack_trace(self, ex):
    buffer = io.StringIO()
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
