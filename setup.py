from setuptools import setup, find_packages

setup(
    name='infinfluxdb',
    version='0.0.1',
    author='Bifer Team',
    description='Base python infrastructure to work with influxdb',
    platforms='Linux',
    install_requires=[line for line in open('requirements.txt')],
    packages=find_packages(exclude=['ez_setup', 'specs', 'tests', 'integration_specs'])
)
