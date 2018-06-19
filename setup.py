import os

from setuptools import setup
import distutils.command.sdist

import setuptools.command.sdist

# Patch setuptools' sdist behaviour with distutils' sdist behaviour
setuptools.command.sdist.sdist.run = distutils.command.sdist.sdist.run

version_info = {}
cwd=os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(cwd, "dxlnmapclient", "_version.py")) as f:
    exec(f.read(), version_info)

dist = setup(
    # Package name:
    name="dxlnmapclient",

    # Version number:
    version=version_info["__version__"],

    # Requirements
    install_requires=[
        "dxlclient",
        "dxlbootstrap>=0.1.3"
    ],

    # Package author details:
    author="Camila Stock",

    # License
    license="Apache License 2.0",

    # Keywords
    keywords=['opendxl', 'dxl', 'client', 'nmap'],

    # Packages
    packages=[
        "dxlnmapclient",
        "dxlnmapclient._config",
        "dxlnmapclient._config.sample"],

    package_data={
        "dxlnmapclient._config.sample" : ['*']},

    # Details
    url="https://www.opendxl.com/",

    description="OpenDXL Nmap service",

    long_description=open('README').read(),

    classifiers=[
        "Programming Language :: Python"
    ],
)
