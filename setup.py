#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
from setuptools import setup, find_packages

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name="termtitle",
    version="0.2.0",
    description='A command line program to change macOS terminal title',
    long_description=readme,
    # long_description=README,
    # long_description_content_type="text/markdown",
    # enable ~/.zshrc DISABLE_AUTO_TITLE=”true” in .zshrc
    # https://github.com/pypa/warehouse/issues/2170
    # https://realpython.com/pypi-publish-python-package/
    url='https://github.com/grimmer0125/terminal-title-change',
    author='Grimmer',
    author_email='grimmer0125@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            "termtitle = termtitle.termtitle:change_title"
        ]
    }
)
