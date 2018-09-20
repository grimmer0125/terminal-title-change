from setuptools import setup, find_packages

setup(
    name="termtitle",
    version="1.0",
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            "termtitle = termtitle.termtitle:change_title"
        ]
    }
)
