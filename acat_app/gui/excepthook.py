# -*- coding: utf-8 -*-
"""
import traceback

from datetime import datetime
from io import StringIO
"""
import logging


def excepthook(exc_type, exc_value, tracebackobj):
    """
    Global function to catch unhandled exceptions.

    Parameters
    ----------
    exc_type : str
        exception type
    exc_value : int
        exception value
    tracebackobj : traceback
        traceback object
    """
    """
    separator = "-" * 80
    notice = "The following error was triggered:"

    now = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

    info = StringIO()
    traceback.print_tb(tracebackobj, None, info)
    info.seek(0)
    info = info.read()

    errmsg = f"{exc_type}\t \n{exc_value}"

    sections = [now, separator, errmsg, separator, info]
    msg = "\n".join(sections)

    print("".join(traceback.format_tb(tracebackobj)))
    print("{0}: {1}".format(exc_type, exc_value))

    print(notice)
    print(msg)
    """
    acat_logger = logging.getLogger("rich")
    acat_logger.error(
        "Unexpected exception", exc_info=(exc_type, exc_value, tracebackobj)
    )


"""
    ErrorDialog(
        message=errmsg, trace=msg, title="The following error was triggered"
    ).exec_()
"""
