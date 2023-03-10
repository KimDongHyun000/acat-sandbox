# -*- coding: utf-8 -*-
import argparse
import os
import sys
from base.utils.excepthook import excepthook
from base.utils.logger import set_logger

os.environ["QT_API"] = "pyside6"
os.environ["PYQTGRAPH_QT_LIB"] = "PySide6"
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"


def _cmd_line_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--measurements", nargs="*", help="list of acat's case files")
    return parser


def main(measurements=None):

    sys.excepthook = excepthook
    logger = set_logger()
    parser = _cmd_line_parser()
    args = parser.parse_args(sys.argv[1:])

    # 예외 처리 샘플 코드
    for i in range(1000, -1, -1):
        num = 1 / i
        logger.info(f"1/{i} = {num}")

    print(args)
    sys.exit()


if __name__ == "__main__":
    main()
