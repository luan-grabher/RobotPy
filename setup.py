from setuptools import setup, find_packages

setup(
    name='robotpy',
    version='0.1.1',
    packages=find_packages(include=['robotpy', 'robotpy.*']),
)