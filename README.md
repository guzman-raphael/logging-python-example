# Logging with Python Tutorial

This is an example of how to improve your logging strategy in Python. Starting with `print` and evolving to using the standard `logging` library.

# Good References

- https://docs.python.org/3/library/logging.html#logrecord-attributes
- https://docs.python.org/3/library/logging.html#logging-levels
- https://docs.python.org/3/library/logging.html#logging.Logger.getEffectiveLevel


# Graylog

- Wait until `graylog` service is ready i.e. no more logs updated in `docker-compose`
- Navigate to `http://localhost:9000`
- Login with `admin:datajoint_works`
- Navigate to `System -> Inputs`
- Click `Select input -> GELF UDP`
- Click `Launch new input`
- Supply a `Title`
- Click `Save`
- Run `docker exec -it logging-python-example_log-example_1 ./example.py`
- Click `Show received messages`