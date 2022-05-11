#!/opt/conda/bin/python
import tqdm
import logging
import time
from new_logging import log_format, TqdmToLogger

log = logging.getLogger("Primary")


class CustomLogHandler(logging.Handler):
    def emit(self, log_record):
        log_storage.append(self.format(log_record))


custom_handler = CustomLogHandler()
custom_handler.setFormatter(log_format)

log.addHandler(custom_handler)

WARNING_LIMIT = 2
log_storage = []


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

    raise Exception("Whoops!")
