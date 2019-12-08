# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in mdm_marketing/__init__.py
from mdm_marketing import __version__ as version

setup(
	name='mdm_marketing',
	version=version,
	description='Marketing Management and CRM',
	author='MDM',
	author_email='it@lab51.org',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
