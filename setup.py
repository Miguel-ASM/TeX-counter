# NOTE: This file must remain Python 2 compatible for the foreseeable future,
# to ensure that we error out properly for people with outdated setuptools
# and/or pip.

import sys

min_version = (3, 6)

if sys.version_info < min_version:
    error = """
Python {0} or above is required.
""".format('.'.join(str(n) for n in min_version)),
    sys.exit(error)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pySOM-Miguel-ASM",
    version="0.0.4",
    author="Miguel Angel Simon Martinez",
    author_email="miguel.a.s.martinez@gmail.com",
    description="Python implementation of Schrodinger equation split-step propagators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Miguel-ASM/pysom",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>={}'.format('.'.join(str(n) for n in min_version)),
    install_requires=[
            "numpy>=1.15",
            "scipy>=1.3"
    ],
)
