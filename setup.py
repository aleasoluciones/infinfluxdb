from setuptools import setup, find_packages

setup(
    name='infinfluxdb',
    version='0.0.1',
    author='Bifer Team',
    description='Base python infrastructure to work with influxdb',
    platforms='Linux',
    packages=find_packages(exclude=['ez_setup', 'specs', 'tests', 'integration_specs'])
)
