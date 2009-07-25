#!/usr/bin/python
# -*- coding: utf-8 -*-
# file:setup.py
### setup.py ###

from distutils.core import setup

setup (name='islanger',
		version='0.1',
		description='internet slang language to plain English',
		long_description="""\
iSlanger - a Python program for translation of an internet slang language to a plain English.
		""",
		author="Damjan Dimitrioski",
		author_email="damjandimitrioski@gmail.com",
		url="",
		license='GPL',
		packages=['islanger'],
		package_dir={'islanger': 'src/islanger/'},
		package_data={'islanger': ['src/data/*']},
		scripts=['bin/islangercli.py', 'bin/islangergtk.py']
)
