import logging
from enum import Enum

LOG_FORMAT = r"%(levelname)s %(name)s %(message)s"


class LogLevels(Enum):
    NOTSET = 0
    DEBUG = 10
    INFO = 20
    CRITICAL = 30
    WARNING = 40
    ERROR = 50


def get_log_level_from_count(count: int) -> LogLevels:
    """get_log_level_from_count Dispatch the verbose count to Loglevels enum.

    Parameters
    ----------
    count : int
        Verbose count from CLI

    Returns
    -------
    LogLevels
        Corresponding Enum from the count
    """
    level = LogLevels.ERROR
    if count == 1:
        level = LogLevels.INFO
    if count >= 2:
        level = LogLevels.DEBUG
    return level


def add_stream_logging(logger: logging.Logger, level: LogLevels) -> logging.Logger:
    log_level = logging.getLevelName(level.name)
    stream_handler = logging.StreamHandler()
    stream_formatter = logging.Formatter(LOG_FORMAT)
    stream_handler.setFormatter(stream_formatter)
    stream_handler.setLevel(log_level)
    logger.addHandler(stream_handler)
    return logger


def init_logger(level: LogLevels) -> None:
    """init_logger Init the stream logger for the project.

    Parameters
    ----------
    level : LogLevels
        Enum corresponding to the level we want
    """
    # Root logger
    logger = logging.getLogger(name="{{cookiecutter.project_slug}}")
    debug_level = logging.getLevelName(LogLevels.DEBUG.name)
    logger.setLevel(debug_level)

    # Need to set the root to debug to allow any level in stream
    logger = add_stream_logging(logger, level)
