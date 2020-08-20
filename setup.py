import os
from setuptools import setup

setup(
    name='fastprocess',
    version='2.0.0',
    author='Dylan Stephano-Shachter',
    author_email='dstephanoshachter@gmail.com',
    description=('A fast subprocess library'),
    license='LGPL',
    url='https://github.com/dstathis/fastprocess',
    packages=['fastprocess'],
    python_requires='>=3.8',
    long_description=open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')
    ).read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: POSIX',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
