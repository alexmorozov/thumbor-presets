#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    description = f.read()

setup(
    name="thumbor_presets",
    version='0.1.0',
    url='http://github.com/alexmorozov/thumbor-presets',
    author='Alex Morozov',
    author_email='inductor2000@mail.ru',
    description=description,
    license='MIT',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True,
    install_requires=['thumbor', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics :: Presentation',
    ],
)
