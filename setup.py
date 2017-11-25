from setuptools import setup, find_packages


setup(
    name='scrapy-example',
    version='1.0',
    packages=find_packages(),
    spiders=[
        'kupatana-electronics',
    ],
    entry_points={
        'scrapy': ['settings = components.settings'],
    },
)