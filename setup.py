from setuptools import setup, find_packages


setup(
    name='scrapy-example',
    version='1.0',
    packages=find_packages(),
    scripts=[
        'components/spiders/KupatanaElectronics.py',
    ],
    entry_points={
        'scrapy': ['settings = components.settings'],
    },
)