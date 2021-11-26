from setuptools import find_packages, setup
setup(
    name='easyFiles',
	packages=find_packages(include=['easyFiles']),
    version='0.1.0',
    description='Easy File finding.',
    author='Daan Holleman',
	install_requires=['numpy', 'os'],
)