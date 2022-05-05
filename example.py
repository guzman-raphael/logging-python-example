#!/usr/bin/python3
import os
import logging

logging.basicConfig(
    level=os.environ.get(
        "LOG_LEVEL", "warning"
    ).upper(),  # debug, info, warning, error, critical
    format="[%(asctime)s][%(funcName)-8s][%(levelname)-8s]: %(message)s",
)
WARNING_LIMIT = 2


def job(args: list):
    try:
        if len(args) > WARNING_LIMIT:
            logging.warning(f"Length longer than warning limit ({WARNING_LIMIT}).")
    except TypeError:
        logging.error("Not able to iterate over args")
        return "failed"
    number_args = [_ for _ in args if isinstance(_, int)]
    logging.debug(f"number_args: {number_args}")
    string_args = [_ for _ in args if isinstance(_, str)]
    logging.debug(f"string_args: {string_args}")
    if number_args and string_args:
        logging.info("args consist of both strings and integers!")
    return "success"


def run(args: list):
    logging.info("started run")
    status = job(args)
    logging.debug(f"status: {status}")


if __name__ == "__main__":
    logging.info("script started")
    run(args=[1, "a", 2, "b"])
    run(args=7)
    logging.info("script completed")
