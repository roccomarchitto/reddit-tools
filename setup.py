#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

version = '0.3.0 PRE ALPHA'

with open("README.md", "rb") as f:
    long_desc = f.read().decode("utf-8")

setup(
    name = "reddit-tools",
    packages = ["reddittools"],
    entry_points = {
        "console_scripts": ['reddittools = reddittools.core:main']
    },
    version = version,
    description = "Suite of useful Reddit automation tools",
    long_description = long_desc,
    author = "RM"
    )
