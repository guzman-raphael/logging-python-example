#!/usr/bin/python3
import utils

WARNING_LIMIT = 2


def job(args: list):
    utils.log(message="job", message_type="header", pause_duration=1)
    try:
        if len(args) > WARNING_LIMIT:
            utils.log(message=f"Length longer than warning limit ({WARNING_LIMIT}).")
    except TypeError:
        utils.log(message="Not able to iterate over args")
        return "failed"
    number_args = [_ for _ in args if isinstance(_, int)]
    utils.log(message=f"number_args: {number_args}")
    string_args = [_ for _ in args if isinstance(_, str)]
    utils.log(message=f"string_args: {string_args}")
    if number_args and string_args:
        utils.log(message="args consist of both strings and integers!")
    return "success"


def run(args: list):
    utils.log(message="run", message_type="header", pause_duration=1)
    utils.log(message="started run")
    status = job(args)
    utils.log(message=f"status: {status}")


if __name__ == "__main__":
    utils.log(message="main", message_type="header", pause_duration=1)
    utils.log(message="script started")
    run(args=[1, "a", 2, "b"])
    run(args=7)
    utils.log(message="script completed")
