from setuptools import setup, find_packages


setup(
    name='scrapy-example',
    version='1.0',
    packages=find_packages(),
    scripts=[
        'bin/check_jobs.py',
    ],
    entry_points={
        'scrapy': ['settings = components.settings'],
    },
)