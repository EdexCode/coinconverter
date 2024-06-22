from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'Real-time currency converter'
# Setting up
setup(
    name="coinconverter",
    version=VERSION,
    author="EdexCode",
    author_email="edexcode@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['bs4', 'requests'],
    keywords=['python', 'currency', 'converter', 'realtime', 'convert'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)