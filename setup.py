from setuptools import setup, find_packages

setup(
    name="gc2_lib",
    version="0.1.1",
    author="Antoine Baudoux",
    author_email="abaudoux@gmail.com",
    packages=find_packages(include=['gc2_lib', 'gc2_lib.*']),
)