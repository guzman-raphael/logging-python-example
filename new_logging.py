import os
import sys
import io
import logging
import logging.handlers

log = logging.getLogger("Primary")
log_level = os.environ.get(
    "LOG_LEVEL", "warning"
).upper()  # debug, info, warning, error, critical)
log_format = logging.Formatter(
    "[%(asctime)s][%(funcName)-10s][%(levelname)-8s]: %(message)s"
)

stream_handler = logging.StreamHandler()  # default handler
stream_handler.setFormatter(log_format)

file_handler = logging.handlers.RotatingFileHandler(
    "logs/example.log", maxBytes=50 * 1024**1, backupCount=3
)  # defaults to append to file
file_handler.setFormatter(log_format)

log.setLevel(level=log_level)
log.handlers = [stream_handler, file_handler]


def excepthook(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    if log.getEffectiveLevel() == 10:
        log.debug("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    else:
        log.error(f"Uncaught exception: {exc_value}")


sys.excepthook = excepthook

# https://github.com/tqdm/tqdm/issues/313#issuecomment-267959111
class TqdmToLogger(io.StringIO):
    """
    Output stream for TQDM which will output to logger module instead of
    the StdOut.
    """

    logger = None
    level = None
    buf = ""

    def __init__(self, logger, level=None):
        super(TqdmToLogger, self).__init__()
        self.logger = logger
        self.level = level or logging.INFO

    def write(self, buf):
        self.buf = buf.strip("\r\n\t ")

    def flush(self):
        self.logger.log(self.level, self.buf)
