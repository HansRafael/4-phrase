import logging
import sys

CONFIG_FORMATTER = logging.Formatter('%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s')

def stream_hendler():
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(CONFIG_FORMATTER)
    return handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger.addHandler(stream_hendler())

    return logger

