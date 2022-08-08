import os
from setuptools import setup

BUILD_ID = os.environ.get("BUILD_BUILDID", "0")

setup(
    name="GC2 python libraries",
    version="0.1" + "." + BUILD_ID,
    # Author details
    author="Antoine Baudoux",
    author_email="abaudoux@gmail.com",
    packages=['g2c_lib'],
    setup_requires=[],
)