#!/usr/bin/python
# -*- coding: utf-8 -*-
# file:islangerCli.py

#       islangerCli.py
#       
#       Copyright 2009 Damjan Dimitrioski <damjandimitrioski@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import islanger

def cli ():
	isl = islanger.islangcore._islanger ()
	word = None
	msg = "Tell me your f word> "
	while word != "":
		word = raw_input (msg)
		print (isl.fetcher (word))
cli ()
