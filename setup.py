# setup.py
from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup

setup(
    name="acat_sandbox",
    version="0.1",
    packages=find_packages(where="acat-app"),
    package_dir={"": "gui"},
    py_modules=[splitext(basename(path))[0] for path in glob("gui/*.py")],
)
