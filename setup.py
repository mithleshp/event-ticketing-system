# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='event_ticketing_system',
    version='0.1.0',
    description='Event Ticketing System',
    long_description=readme,
    author='Mithlesh Pandey',
    author_email='mithlesh.pandey@gmail.com',
    url='https://github.com/kennethreitz/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

