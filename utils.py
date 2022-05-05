import time


def log(message: str, pause_duration: int = 0, message_type: str = "message"):
    if message_type == "message":
        print(f"\n -> {message}", flush=True)
    elif message_type == "header":
        print(f"\n=== {message.upper()} ===", flush=True)
    if pause_duration:
        time.sleep(pause_duration)
