import io
import logging
import traceback
import types


def stack_trace(self, ex):
    buffer = io.StringIO()
    traceback.print_exception(type(ex), ex, ex.__traceback__, file=buffer)
    self.error(buffer.getvalue())


def get_logger(log_level):
    if 'my_logger' in logging.Logger.manager.loggerDict:
        return logging.getLogger('my_logger')
    else:
        logging.basicConfig(filename='application.log',
                            level=log_level,
                            format='%(asctime)s %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger('my_logger')
        logger.stack_trace = types.MethodType(stack_trace, logger)
        return logger
