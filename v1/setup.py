#!/usr/bin/env python

import sys

from setuptools import setup, find_packages

from wagtailapi_legacy_v1 import __version__


setup(
    name='wagtailapi_legacy_v1',
    version=__version__,
    description='',
    author='Karl Hobley',
    author_email='karl@kaed.uk',
    url='',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    install_requires=[
        'six>=1.10.0',
    ],
    zip_safe=False,
)