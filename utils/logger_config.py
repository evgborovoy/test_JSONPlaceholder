import logging
import sys


def configure_logger(name: str = "api_testing") -> logging.Logger:
    log = logging.getLogger(name)
    log.setLevel(logging.INFO)

    if not log.handlers:
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(logging.DEBUG)

        log.addHandler(stream_handler)

    return log


logger = configure_logger()
