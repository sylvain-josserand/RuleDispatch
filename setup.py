#!/usr/bin/env python
"""Distutils setup file

RuleDispatch is Copyright 2004, 2005 by Phillip J. Eby; all rights reserved.
This software may be used under the same terms as Python or Zope, with NO
WARRANTIES OF ANY KIND WHATSOEVER.
"""

from Cython.Distutils import build_ext

import ez_setup, sys
ez_setup.use_setuptools()

from setuptools import setup, Feature, Extension

speedups = Feature(
    "optional C speed-enhancement modules",
    standard = True,
    ext_modules = [
        Extension("dispatch._d_speedups", ["dispatch/_d_speedups.pyx"]),
    ]
)

setup(
    name="RuleDispatch",
    version="0.5a1",
    description="Rule-based Dispatching and Generic Functions",
    long_description = open('README.txt').read(),
    author="Phillip J. Eby",
    author_email="peak@eby-sarna.com",
    license="PSF or ZPL",
    install_requires=[
        'PyProtocols>=1.0a0dev-r2302',
        'Extremes>=1.1',
        'Cython>=0.21'
    ],
    #url = "http://pypi.python.org/pypi/RuleDispatch",
    #download_url = "http://peak.telecommunity.com/snapshots/",
    zip_safe    = sys.version>='2.3.5',
    test_suite  = 'dispatch.tests.test_suite',
    package_data = {'': ['*.txt']},
    packages    = ['dispatch'],
    features    = {'speedups': speedups},
    cmdclass={'build_ext': build_ext},
)

