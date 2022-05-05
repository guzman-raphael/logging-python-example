#!/usr/bin/python3
import os
import logging
import logging.handlers

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
    "logs/example.log", maxBytes=300, backupCount=5
)  # defaults to append to file
file_handler.setFormatter(log_format)

log.setLevel(level=log_level)
log.handlers = [stream_handler, file_handler]

WARNING_LIMIT = 2


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
    return "success"


def run(args: list):
    log.info("started run")
    status = job(args)
    log.debug(f"status: {status}")


if __name__ == "__main__":
    log.info("script started")
    run(args=[1, "a", 2, "b"])
    run(args=7)
    log.info("script completed")
