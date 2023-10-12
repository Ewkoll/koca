#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: ewkoll ideath@operatorwrold.com
Date: 2023-09-18 19:40:37
LastEditors: ewkoll
LastEditTime: 2023-10-12 15:25:28
Description: 
Copyright (c) 2023 by ewkoll email: ideath@operatorwrold.com, All Rights Reserved.
'''
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="koca",
    version="0.0.4",
    author="ewkoll",
    author_email="ideath@operatorworld.com",
    description="A small koca package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ewkoll/koca",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)