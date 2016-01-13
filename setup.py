from __future__ import unicode_literals
from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django_extra_migrations',
    version='0.0.6',

    description='Extra migration classes for django',
    long_description=long_description,
    url='https://github.com/xacce/django_extra_migrations',
    author='Xacce',
    author_email='thiscie@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='django migrations permissions models',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['progressbar2'],
)
