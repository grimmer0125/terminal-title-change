from setuptools import setup, find_packages

setup(
    name="termtitle",
    version="0.1.0",
    description = 'A command line program to change macOS terminal\'s title',
    long_description = open('README.rst').read(),
    url = 'https://github.com/grimmer0125/terminal-title-change',
    author='Grimmer',
    license='MIT',
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            "termtitle = termtitle.termtitle:change_title"
        ]
    }
)
