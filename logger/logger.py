import logging

APP_LOGGER_NAME = 'APP'


def setup_applevel_logger(logger_name=APP_LOGGER_NAME, file_name="app_debug.log"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "[%(levelname)-s]:%(filename)s %(funcName)s [Line %(lineno)s] - %(message)s")

    fh = logging.FileHandler(file_name, mode='w')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger


def get_logger(module_name):
    return logging.getLogger(APP_LOGGER_NAME).getChild(module_name)