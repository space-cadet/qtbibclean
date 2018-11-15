""" setup.py - Script to install package using distutils

For help options run:
$ python setup.py help

"""
#Author: Ian Huston


from setuptools import setup
from pyinspire import pyinspire

###############
VERSION = pyinspire.__version__


setup_args = dict(name='pyinspire',
                  version=VERSION,
                  author='Ian Huston',
                  author_email='ian.huston@gmail.com',
                  url='https://bitbucket.org/ihuston/pyinspire',
                  packages=['pyinspire'],
                  scripts=['pyinspire/pyinspire.py'],
                  package_data={},
                  license="Modified BSD license",
                  description="""Pyinspire queries the INSPIRE HEP database and returns
either BiBTeX or normal text results""",
                  long_description=open('README.txt').read(),
                  classifiers=["Topic :: Utilities",
                               "Intended Audience :: Science/Research",
                               "License :: OSI Approved :: BSD License",
                               "Operating System :: OS Independent",
                               "Programming Language :: Python",
                               "Programming Language :: Python :: 2.7",
                               "Programming Language :: Python :: 3.4",
                               ],
                  install_requires=["beautifulsoup4"],
                  )

if __name__ == "__main__":
    setup(**setup_args)
