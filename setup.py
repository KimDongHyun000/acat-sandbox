# -*- coding: utf-8 -*-

from pathlib import Path
from setuptools import find_packages, setup

PROJECT_PATH = Path(__file__).parent
print(PROJECT_PATH)

with (PROJECT_PATH / "requirements_dev.txt").open("rt", encoding="euc-kr") as req_file:
    install_requires = [line.strip() for line in req_file.readlines()]


def _get_version():
    with PROJECT_PATH.joinpath("acat_app", "version.py").open() as f:
        line = next(line for line in f if line.startswith("__version__"))
    version = line.partition("=")[2].strip()[1:-1]
    return version


setup(
    name="acat",
    version=_get_version(),
    description="ACAT - Automated Car-accident Analysis Tool",
    license="LGPLv3+",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: LGPLv3+",
        "Programming Language :: Python :: 3.11",
    ],
    install_requires=install_requires,
    extras_require={
        "gui": [
            "lxml",
            "natsort",
            "psutil",
            "PySide6",
            "pyqtgraph>=0.12.4",
            "pyqtlet2>=0.8.0",
            "scipy<1.8.0",
        ]
    },
    packages=find_packages(
        include="acat_app*",
    ),
    package_dir={"acat-sandbox": "acat_app"},
    package_data={
        "acat-sandbox": [
            "acat_app/3rdparty/*",
            "acat_app/base/*",
            "acat_app/gui/ui/*.ui",
        ]
    },
    include_package_data=True,
    entry_points={"console_scripts": ["acat_app = acat_app.gui.acat_app:main [gui]"]},
)
