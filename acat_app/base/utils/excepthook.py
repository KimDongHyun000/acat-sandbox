# -*- coding: utf-8 -*-
import logging


def excepthook(exc_type, exc_value, tracebackobj):
    acat_logger = logging.getLogger("rich")
    acat_logger.error(
        "Unexpected exception", exc_info=(exc_type, exc_value, tracebackobj)
    )


"""
    ErrorDialog(
        message=errmsg, trace=msg, title="The following error was triggered"
    ).exec_()
"""
