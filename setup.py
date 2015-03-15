import sys
from setuptools import setup , find_packages

exec(open("smbl/version.py").read())

setup(
	name = 'smbl',
	packages = [
		'smbl',
		'smbl.fasta',
		'smbl.prog',
		'smbl.prog.plugins',
	],
	package_dir = {
		"smbl" : "smbl",
		"smbl.fasta" : "smbl/fasta",
		"smbl.prog": "smbl/prog",
		"smbl.prog.plugins": "smbl/prog/plugins",
	},
	package_data = {
		"smbl" : ["*.snake"],
		"smbl.fasta" : ["*.snake"],
		"smbl.prog" : ["*.snake"],
	},
	version = __version__,
	description = 'SnakeMake Bioinformatics Library',
	long_description = """\
SnakeMake Bioinformatics Library
--------------------------------

A library for SnakeMake pipelines which makes possible to install various bioinformatics
tools and download data (e.g., in FASTA format). See http://github.com/karel-brinda/smbl
for details.

Copyright (c) 2015 Karel Břinda <karel.brinda@gmail.com> (see LICENSE)
""",
	install_requires=[
		'snakemake',
		'termcolor',
	],
	zip_safe=False,
	author = 'Karel Břinda',
	author_email = 'karel.brinda@gmail.com',
	url = 'http://github.com/karel-brinda/smbl',
	license = "MIT",
	#download_url = 'https://github.com/karel-brinda/smbl/tarball/0.0.1',
	keywords = ['Snakemake', 'bioinformatics','pipelines','Next Generation Sequencing'],
	classifiers = [
		"Development Status :: 4 - Beta",
		"Environment :: Console",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Programming Language :: Python :: 3",
		"Topic :: Scientific/Engineering :: Bio-Informatics"
	],
)
