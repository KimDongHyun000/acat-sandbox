# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger("acat-app")
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
console = logging.StreamHandler()
console.setFormatter(formatter)
console.setLevel(logging.DEBUG)
logger.addHandler(console)
logger.setLevel(logging.ERROR)
