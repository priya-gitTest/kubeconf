import io
import os
from setuptools import setup, find_packages

# Use README for long description
here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


setup(
    name='kubeconf',
    version='0.0.1',
    description='Simple tool for managing your kubeconfig.',
    author='Zach Sailer',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email='zachsailer@gmail.com',
    url='https://github.com/Zsailer/kubeconf',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)