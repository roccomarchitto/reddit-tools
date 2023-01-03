#!/usr/bin/python3
# -*- coding: utf-8 -*-

__version__ = "0.2.0 DEV BANNER"

import sys
from . import m

def main():
    print(f"Version {__version__}")
    print(f"Args passed: {sys.argv[1:]}")
