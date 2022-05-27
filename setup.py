#!/usr/bin/env python3
# coding=utf-8

from setuptools import setup
from os import system

version = '1.1.1'

setup(
    name='turtle_pil',
    packages=['turtle_pil'],
    install_requires=[
        'pillow',
    ],
    version=version,
    description='Turtle operations on the top of PIL',
    long_description='Turtle operations on the top of PIL',
    author='Jordi Petit',
    url='https://github.com/jutge-org/pil-turtle',
    download_url='https://github.com/jutge-org/pil-turtle/tarball/{}'.format(version),
    keywords=['jutge', 'jutge.org', 'education', 'turtle', 'PIL'],
    license='Apache',
    zip_safe=False,
    include_package_data=True,
    setup_requires=['setuptools'],
    entry_points={
        'console_scripts': [
        ]
    },
    scripts=[
    ]
)


# Steps to try new version:
# -------------------------
#
# pip3 uninstall --yes pil-turtle
# pip3 install .

# Steps to distribute new version:
# --------------------------------
#
# see upload.sh script
