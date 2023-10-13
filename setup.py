from setuptools import setup, find_packages

setup(
    name='veeam_sync',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'watchdog',
    ],
)
