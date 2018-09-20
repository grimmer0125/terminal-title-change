#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
from setuptools import setup, find_packages

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name="termtitle",
    version="0.1.1",
    description = 'A command line program to change macOS terminal\'s titles',
    long_description=readme,
    url='https://github.com/grimmer0125/terminal-title-change',
    author='Grimmer',
    license='MIT',
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            "termtitle = termtitle.termtitle:change_title"
        ]
    }
)
