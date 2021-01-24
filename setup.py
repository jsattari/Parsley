#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='Parsley',
    version='1.0',
    author='John Sattari',
    author_email='jsattari3@gmail.com',
    packages=['parsley'],
    install_requires=['pandas', 'fire'],
    url='https://github.com/jsattari/Parsley',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': [
            'parsley = parsley.parsley:main'
        ]
    },
)
