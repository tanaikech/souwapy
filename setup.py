#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__author__ = 'Kanshi TANAIKE'

setup(
    name='souwapy',
    version='1.1.1',
    description='This is a library for summing array elements with high speed by new algorithm.',
    author='Kanshi TANAIKE',
    author_email='tanaike@hotmail.com',
    url='https://github.com/tanaikech/souwapy',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(),
    keywords=['array', 'sum', 'speed', 'algorithm', 'pyramid', 'new algorithm'],
    license='MIT License'
)
