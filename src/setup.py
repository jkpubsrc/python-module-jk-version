################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"License :: OSI Approved :: Apache Software License",
		"Programming Language :: Python :: 3",
	],
	description = "This python module provides a version class. Instances of this class may be used in representing and version numbers and compare them.",
	include_package_data = False,
	install_requires = [
	],
	keywords = [
		"version",
		"versioning",
	],
	license = "Apache2",
	name = "jk_version",
	packages = [
		"jk_version",
	],
	version = "0.2022.2.11",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)
