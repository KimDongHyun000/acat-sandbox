# -*- coding: utf-8 -*-
import logging
import platform

from logging.handlers import RotatingFileHandler

from rich.logging import RichHandler

LOG_PATH = "./logs/acat_app.log"
RICH_FORMAT = "[%(filename)s:%(lineno)s] >> %(message)s"
FILE_HANDLER_FORMAT = "[%(asctime)s]\t%(levelname)s\t[%(filename)s:%(funcName)s:\
    %(lineno)s]\t>> %(message)s"


def set_logger() -> logging.Logger:
    logging.basicConfig(
        level="NOTSET", format=RICH_FORMAT, handlers=[RichHandler(rich_tracebacks=True)]
    )
    logger = logging.getLogger("rich")

    rot_file_handler = RotatingFileHandler(
        LOG_PATH, mode="a", maxBytes=1024, backupCount=5
    )
    if platform.system() == "Windows":
        import msvcrt
        import win32api
        import win32con

        win32api.SetHandleInformation(
            msvcrt.get_osfhandle(rot_file_handler.stream.fileno()),
            win32con.HANDLE_FLAG_INHERIT,
            0,
        )
    rot_file_handler.setFormatter(logging.Formatter(FILE_HANDLER_FORMAT))
    logger.addHandler(rot_file_handler)

    """
    file_handler = logging.FileHandler(LOG_PATH, mode="a", encoding="utf-8")
    file_handler.setFormatter(logging.Formatter(FILE_HANDLER_FORMAT))
    logger.addHandler(file_handler)
    """

    return logger
