#!/usr/bin/env python
import os
import sys

try:
    from setuptools import setup
    from setuptools.command.test import test as TestCommand

    class PyTest(TestCommand):
        def finalize_options(self):
            TestCommand.finalize_options(self)
            self.test_args = []
            self.test_suite = True

        def run_tests(self):
            # import here, because outside the eggs aren't loaded
            import pytest
            errno = pytest.main(self.test_args)
            sys.exit(errno)

except ImportError:

    from distutils.core import setup

    def PyTest(x):
        x

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
long_description = f.read()
f.close()

setup(
    name='pubsubsql',
    version="1.0.0",
    description='Python client for PubSubSQL database',
    long_description=long_description,
    url='http://github.com/pubsubsql/pss-py',
    author='Oleg Rabaev',
    author_email='info@pubsubsql.com',
    maintainer='Oleg Rabaev',
    maintainer_email='info@pubsubsql.com',
    keywords=['PubSubSQL', 'database'],
    license='Apache2.0',
    packages=['pubsubsql', 'pubsubsql.net'],
    tests_require=['pytest>=2.5.0'],
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
