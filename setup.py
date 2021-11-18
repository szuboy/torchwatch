# !/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import setuptools
from setuptools import setup

with open('requirements.txt', 'r') as fp:
    requirements = list(filter(bool, (line.strip() for line in fp)))

with open('README.rst') as fp:
    long_description = fp.read()

with open('version.txt') as fp:
    version = fp.readline().strip()

package_data = []

package_name = 'torchwatch'

if __name__ == '__main__':
    setup(
        name=package_name,
        url='https://github.com/szuboy/torchwatch#readme',
        project_urls={
            'Documentation': 'https://torchwatch.readthedocs.io/',
            'Github': 'https://github.com/szuboy/torchwatch'
        },
        author='szuboy',
        author_email='szujeremy@gmail.com',
        version=version,
        packages=setuptools.find_packages(),
        package_data={'torchwatch': package_data},
        description='basic block built with pytorch',
        long_description=long_description,
        long_description_content_type='text/markdown',
        license='Apache License',
        keywords='torch torchwatch basic-block module deep-learning Residual Inception SE_block',
        install_requires=requirements,
        python_requires='>=3.0'
    )
