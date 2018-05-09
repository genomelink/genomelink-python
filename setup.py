import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='genomelink',
    version='0.2.0',
    description='GENOME LINK',
    long_description='',
    author='GENOME LINK',
    author_email='',
    url='https://github.com/genomelink/genomelink-python',
    packages=['genomelink', 'genomelink.resource'],
    install_requires=[
        'requests',
        'requests_oauthlib'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ])
