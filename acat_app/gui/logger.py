# -*- coding: utf-8 -*-
import logging
import logging.handlers

from rich.logging import RichHandler

LOG_PATH = "./acat_app.log"
RICH_FORMAT = "[%(filename)s:%(lineno)s] >> %(message)s"
FILE_HANDLER_FORMAT = "[%(asctime)s]\t%(levelname)s\t[%(filename)s:%(funcName)s:\
    %(lineno)s]\t>> %(message)s"


def set_logger() -> logging.Logger:
    logging.basicConfig(
        level="NOTSET", format=RICH_FORMAT, handlers=[RichHandler(rich_tracebacks=True)]
    )
    logger = logging.getLogger("rich")

    file_handler = logging.FileHandler(LOG_PATH, mode="a", encoding="utf-8")
    file_handler.setFormatter(logging.Formatter(FILE_HANDLER_FORMAT))
    logger.addHandler(file_handler)

    return logger
