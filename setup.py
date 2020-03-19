#!/usr/bin/env python

from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='bloodytests',
    version='0.1',
    author='Bloodmallet(EU)',
    author_email='kruse.peter.1990@gmail.com',
    description='Some additional features to standard unittest library',
    long_description=readme(),
    url='https://github.com/Bloodmallet/bloodytests',
    packages=['bloodytests'],
    package_data={
        "": ["*.md",],
    },
    python_requires='>=3.6',
    license='GNU GENERAL PUBLIC LICENSE',
)
