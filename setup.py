from setuptools import setup, find_packages

setup(
    name="terminaltitle",
    version="1.0",
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            "terminaltitle = changetitle.changetitle:change_title"
        ]
    }
)
