"""
setup.py for ClassificaIO package
"""
from setuptools import setup, find_packages
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description=f.read()

setup(
    name='ClassificaIO',
    packages=find_packages(),
    version='1.0.0',
    description='Graphical User Interface for machine learning classification algorithms from scikit-learn',
    long_description=long_description,
    author='G. Mias Lab',
    author_email='gmiaslab@gmail.com',
    license='MIT',
    url='https://github.com/gmiaslab/ClassificaIO',
    download_url='https://github.com/gmiaslab/ClassificaIO/archive/1.0.0.tar.gz',
    keywords=['machine learning', 'classification','bioinformatics'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Topic :: Education',
        'Topic :: Utilities',
        ],
    install_requires=[
        'nltk>=3.2.5',
        'Pillow>=4.3',
        'pandas>=0.21',
        'numpy>=1.13',
        'scikit-learn>=0.19.1'],
    zip_safe=False
)