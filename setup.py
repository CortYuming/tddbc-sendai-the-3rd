# -*- coding: utf-8 -*-
try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command


setup(
    name='The skeleton of py.test for python users.',
    version='0.0.1',
    url='https://github.com/SendayPy/tddbc-sendai-the-3rd.git',
    author='SendaiPy',
    author_email='nishi.tak@gmail.com',
    description='The skeleton of py.test for python users',
    license='MIT',
    packages=[],
    package_data={},
    scripts=[''],
    test_require=['pytest'],
    cmdclass={'test': PyTest},
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
