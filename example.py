#!/usr/bin/python3
WARNING_LIMIT = 2


def job(args: list):
    print("=== JOB ===", flush=True)
    try:
        if len(args) > WARNING_LIMIT:
            print(f"Length longer than warning limit ({WARNING_LIMIT}).", flush=True)
    except TypeError:
        print("Not able to iterate over args", flush=True)
        return "failed"
    number_args = [_ for _ in args if isinstance(_, int)]
    print(f"number_args: {number_args}", flush=True)
    string_args = [_ for _ in args if isinstance(_, str)]
    print(f"string_args: {string_args}", flush=True)
    if number_args and string_args:
        print("args consist of both strings and integers!", flush=True)
    return "success"


def run(args: list):
    print("=== RUN ===", flush=True)
    print(f"started run", flush=True)
    status = job(args)
    print(f"status: {status}", flush=True)


if __name__ == "__main__":
    print("=== MAIN ===", flush=True)
    print(f"script started", flush=True)
    run(args=[1, "a", 2, "b"])
    run(args=7)
    print(f"script completed", flush=True)
