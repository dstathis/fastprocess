import os
from setuptools import setup

setup(
    name = 'fastprocess',
    version = '0.1.0',
    author = 'Dylan Stephano-Shachter',
    author_email = 'dstephanoshachter@gmail.com',
    description = ('A fast subprocess library'),
    license = 'LGPL',
    url = 'https://github.com/dstathis/fastprocess',
    packages = ['fastprocess'],
    long_description = open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')
    ).read()
)
