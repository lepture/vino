#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
kwargs = {}
major, minor = sys.version_info[:2]
if major >= 3:
    kwargs['use_2to3'] = True

from setuptools import setup
install_requires = []
try:
    import argparse  # python 2.7+ support argparse
except ImportError:
    install_requires.append('argparse')

kwargs['install_requires'] = install_requires
kwargs['packages'] = ['vino']

import vino
from email.utils import parseaddr
author, author_email = parseaddr(vino.__author__)

setup(
    name='vino',
    version=vino.__version__,
    author=author,
    author_email=author_email,
    #url=vino.__homepage__,
    description='Vino Is Not ORM',
    long_description=open('README.rst').read(),
    license='BSD License',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: Implementation :: CPython',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries',
        'Topic :: Database :: Front-Ends',
    ],
    **kwargs
)
