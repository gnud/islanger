#       islangcore.py
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

import pickle
import traceback
from os.path import exists
from os import mkdir
from os.path import expanduser
from os.path import join

homepath = join(expanduser("~"), ".islanger")
dicname = "slang.dic"

class _islanger:
	def __init__ (self):
		global dicname
		self.dicName = ""
		try:
			print ":: Starting iSlanger Core ::"
			self.dicName = join(homepath, dicname)
		except Exception:
			logpath = join(homepath, "errlog.txt")
			print (logpath)
			traceback.print_exc(file=open(logpath,"a"))
		if not exists (homepath): self.mkuserData()
		try:
			self.pair = {}
			self.loadDic ()
		except IOError:
			print (":: Error: the needed dictionary %s is not found,\n please make one with the dictionary builder. ::" % self.dicName)
			logpath = join(homepath, "errlog.txt")
			print (logpath)
			traceback.print_exc(file=open(logpath,"a"))

	def mkuserData(self):
		mkdir (homepath)

	def loadDic (self):
		print (":: Filling the dictionary ::")
		file = open(self.dicName, "r")
		self.pair = pickle.load(file)
		file.close()

	def findValue (self, val): return self.pair[val]
	def findKey (self, val):
		keys = []
		rez = [keys.append([k, self.findValue(k)]) for k, v in self.pair.iteritems() if k.startswith(val)][0]
		return keys

	def fetcher (self, word):
		#forms = {"*"}
		if word:
			try: value = self.findKey (word); return (value)
			except Exception: traceback.print_exc(file=open(logpath,"a"))

# Debug
#print (_islanger().fetcher ("dude"))
#print (_islanger().fetcher ("fu"))

