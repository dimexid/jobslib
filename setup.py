
import sys

from pathlib import Path
from runpy import run_path

from setuptools import setup, find_packages

description = 'Library for launching tasks in parallel environment'

try:
    with open('README.md', 'rt') as f:
        long_description = f.read()
except Exception:
    long_description = description

version_file = Path(__file__).parent / 'jobslib' / 'version.py'
if sys.version_info < (3, 6):
    version_file = str(version_file)
version = run_path(version_file)['VERSION']

setup(
    name='jobslib',
    version=version,
    author='Seznam.cz a.s.',
    author_email='doporucovani-vyvoj@firma.seznam.cz',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='BSD',
    url='https://gitlab.kancelar.seznam.cz/doporucovani/recass',  # TODO:
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
    packages=find_packages(),
    zip_safe=True,
    install_requires=[
        'cached-property',
        'colored<1.3',
        'objectvalidator',
        'python-consul2',
        'szn-doporucovani-influxdb-wrapper',
    ],
    entry_points={
        'console_scripts': [
            'runjob = jobslib.main:main',
        ]
    },
)
