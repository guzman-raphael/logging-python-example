#!/opt/conda/bin/python
import os
import logging
import logging.handlers
import tqdm
import io
import time

log = logging.getLogger("Primary")
log_level = os.environ.get(
    "LOG_LEVEL", "warning"
).upper()  # debug, info, warning, error, critical)
log_format = logging.Formatter(
    "[%(asctime)s][%(funcName)-8s][%(levelname)-8s]: %(message)s"
)

stream_handler = logging.StreamHandler()  # default handler
stream_handler.setFormatter(log_format)

file_handler = logging.handlers.RotatingFileHandler(
    "logs/example.log", maxBytes=50 * 1024**1, backupCount=3
)  # defaults to append to file
file_handler.setFormatter(log_format)


class CustomLogHandler(logging.Handler):
    def emit(self, log_record):
        log_storage.append(self.format(log_record))


custom_handler = CustomLogHandler()
custom_handler.setFormatter(log_format)

log.setLevel(level=log_level)
log.handlers = [stream_handler, file_handler, custom_handler]

WARNING_LIMIT = 2
log_storage = []

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


def job(args: list):
    try:
        if len(args) > WARNING_LIMIT:
            log.warning(f"Length longer than warning limit ({WARNING_LIMIT}).")
    except TypeError:
        log.exception("Not able to iterate over args")
        return "failed"
    number_args = [_ for _ in args if isinstance(_, int)]
    log.debug(f"number_args: {number_args}")
    string_args = [_ for _ in args if isinstance(_, str)]
    log.debug(f"string_args: {string_args}")
    if number_args and string_args:
        log.info("args consist of both strings and integers!")

    progress_total = 30
    with tqdm.tqdm(
        total=progress_total,
        file=TqdmToLogger(log, level=logging.INFO),
        # mininterval=2,
    ) as pbar:
        for i in range(progress_total):
            log.info(f"processing: {i}")
            time.sleep(0.1)
            pbar.update(1)

    return "success"


def run(args: list):
    # print(f"log_storage: {log_storage}", flush=True)
    log.info("started run")
    status = job(args)
    log.debug(f"status: {status}")


if __name__ == "__main__":
    log.info("script started")
    run(args=[1, "a", 2, "b"])
    run(args=7)
    log.info("script completed")
