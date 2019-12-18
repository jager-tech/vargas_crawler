from setuptools import Command, find_packages, setup

required_modules = []
with open('requirements.txt') as file:
    required_modules = [line.strip() for line in file]

development_modules = []
with open('requirements-dev.txt') as file:
    development_modules = [line.strip() for line in file]

NAMESPACE_PACKAGES = ['jager']

setup(
    name='vargas_crawler',
    version='0.0.1',
    packages=find_packages('src', exclude=['*_test.py']),
    package_dir={'': 'src'},
    namespace_packages=['vargas_crawler'],
    install_requires=required_modules,
    extras_require={'dev': development_modules})
