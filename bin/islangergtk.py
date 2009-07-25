#!/usr/bin/python
# -*- coding: utf-8 -*-
# file:islangerGtk.py

#       islangerGtk.py
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
from gtk import VBox, HBox, Window, Button, CheckButton, Frame, ListStore, CellRendererText, TreeViewColumn, ScrolledWindow, TreeView, Entry
from gtk import main, main_quit, SHADOW_ETCHED_IN, POLICY_AUTOMATIC, POLICY_AUTOMATIC, WIN_POS_CENTER

try:
	import locale; loc = locale.getlocale ()[0]
except Exception: pass
loc = "mk_MK"

# TODO: gettext support
gtenterSlangMK = "Внеси Сленг:"
gtcnumberMK = "Р.Б"
gtkeyMK = "Клуч"
gtvalueMK = "Вредност"
gtclearMK = "Бриши Резултати"

gtenterSlangEN = "Enter your slang:"
gtcnumberEN = "#"
gtkeyEN = "Key"
gtvalueEN = "Value"
gtclearEN = "Clear Results"

if loc == "mk_MK": gtenterSlang = gtenterSlangMK; gtcnumber = gtcnumberMK; gtkey = gtkeyMK; gtvalue = gtvalueMK; gtclear = gtclearMK
else: gtenterSlang = gtenterSlangEN; gtcnumber = gtcnumberEN; gtkey = gtkeyEN; gtvalue = gtvalueEN; gtclear = gtclearEN

class widgetMaker ():
	def __init__ (self):
		self.br = 0
	def get_icon(self, name): return icon_theme_get_default().load_icon (name, 32, 32)
	def hb (self, widgets, homogeneous = False, spacing = 0):
		self.br +=1
		_name = "a%s" % self.br
		_hb = HBox ()
		_hb.set_name (_name)
		if len (widgets) > 1:
			for _child in widgets:
				#print (type(_child))
				_hb.pack_start (_child, homogeneous, spacing)
		else: _hb.pack_start (widgets[0], homogeneous, spacing)
		_hb.set_border_width(5); _hb.show_all()
		return _hb

	def vb (self, widgets, homogeneous = False, spacing = 0):
		self.br +=1
		_name = "vb%s" % self.br
		#print (_name)
		_vb = VBox ();
		_vb.set_name (_name)
		#print (len (widgets))
		if len (widgets) > 1:
			for _child in widgets: _vb.pack_start (_child, homogeneous, spacing)
		else: _vb.pack_start (widgets[0], homogeneous, spacing)
		_vb.set_border_width(1); _vb.show_all ()
		return _vb
	def ram (self, widget, name):
		self.br +=1
		_name = "a%s" % self.br
		frm = Frame (name)
		frm.set_name (_name)
		frm.add (widget)
		return frm

	def lb (self, name): return Label (name)
	def ent (self,  signal):
		_ent = Entry ()
		_ent.connect ("activate", signal)
		return _ent

	def btnMaker (self, click, name, icon = None):
		b = Button (name)
		try:
			img = Image()
			img.set_from_icon_name	("calc", 1)
			b.set_image (img)
		except Exception: pass
		b.connect ("clicked", click)
		return b

class islangerGtk(Window):
	def __init__(self):
		super(islangerGtk, self).__init__()
		self.isl = islanger.islangcore._islanger ()
		self.store = self.create_model()
		self.br = 1
		self.posledno = ""
		#self.generateModel ([])
		self.wm = widgetMaker ()
		self.__widgets__ ()	# Generating every posible component
		self.prozor ()
	def __widgets__ (self):
		self.baraj = self.wm.btnMaker (self.najduvach, "V")
		self.poim = self.wm.ent (self.najduvach)
		self.chisti = self.wm.btnMaker (self.clearTable, gtclear)

	def najdiSteblo (self):
		v = VBox ()
		c1 = self.wm.hb((self.poim, self.baraj))
		v.pack_start(c1, False, 0)
		#print (type(v))
		return self.wm.ram(v, gtenterSlang)

	def drvoSteblo (self):
		vb = VBox ()
		hb = HBox ()
		hb.pack_start (self.chisti, False)
		vb.pack_start (self.table (), True)
		vb.pack_start (hb, False)

		return vb

	def prozor (self):
		self.set_size_request(300, 300)
		self.set_position(WIN_POS_CENTER)
		self.connect("destroy", self.quit) #self.connect("destroy", self.die)
		self.set_title("iSlanger")
		try: self.set_icon (self.wm.get_icon ("text-template"))
		except: pass
		#self.add (self.wm.vb((self.najdiSteblo (), self.drvoSteblo () ) ))
		self.add (self.wm.vb((self.najdiSteblo (), self.drvoSteblo ()), True, 1))
		#self.add(self.wm.vb ((self.table())))
		self.show_all ()

	def generateModel (self, items):
		for item in items:
			self.store.append([item[0], item[1],item[2]])


	def create_model(self):
		#task1 = [('Бриши windows', False), ('Бриши Program Files', False)]
		store = ListStore(int, str, str)
		#br = 1
		#for task in task1:
		#	store.append([br, task[0],task[1]])
		#task[1]]);
		#br+=1
		return store

	def create_columns(self, treeView):
		numbering = CellRendererText()
		column = TreeViewColumn(gtcnumber, numbering, text=0)
		column.set_sort_column_id(0)
		treeView.append_column(column)

		tasking = CellRendererText()
		column = TreeViewColumn(gtkey, tasking, text=1)
		column.set_sort_column_id(1)
		treeView.append_column(column)

		values = CellRendererText()
		column = TreeViewColumn(gtvalue, values, text=2)
		column.set_sort_column_id(2)
		treeView.append_column (column)

	def on_activated(self, widget, row, col):
		model = widget.get_model()
		#text = model[row][0] + ", " + model[row][1] + ", " + model[row][2]
		#self.statusbar.push(0, text)
	def focus_in(self, widget, event, adj):
		print ("ff")
		alloc = widget.get_allocation()
		if alloc.y < adj.value or alloc.y > adj.value + adj.page_size:
			adj.set_value(min(alloc.y, adj.upper-adj.page_size))

	def clearTable (self, widget):
		if len(self.store): print (":: Cleaning our table ::"); self.store.clear()

	def table (self):
		sw = ScrolledWindow()
		sw.set_shadow_type(SHADOW_ETCHED_IN)
		sw.set_policy(POLICY_AUTOMATIC, POLICY_AUTOMATIC)

		#self.tw.set_headers_clickable(active)
		tw = TreeView(self.store)
		headers_visible = tw.get_headers_visible()
		tw.set_headers_visible(headers_visible)

		#tw.set_rules_hint(True)
		#tw.connect('focus_in_event', self.focus_in, adj)
		#tw.connect('row-activated', self.focus_in, adj)

		self.create_columns(tw)
		sw.add(tw)
		sw.show_all()
		#return self.wm.hb((sw), homogeneous = True)
		return sw

	def najduvach (self, widget):
		temp = []
		word = self.poim.get_text ().lower()
		if self.posledno != word:
			#print (type(word.upper()))
			rword = self.isl.fetcher (word)
			if rword != None:
				#print (rword.upper())
				#print (type(rword))
				#print (type(rword))
				#print (rword)
				# list rezults
				for w in rword:
					temp.append([self.br, w[0].upper(), w[1].upper()])
					self.br +=1
				# only string rezults
				#temp.append([self.br, word.upper(), rword.upper()])
				self.generateModel (temp)

			self.posledno = word
			self.poim.grab_focus()

	def quit(self, widget):
		main_quit()
		return True

def Main():
	islG = islangerGtk()
	main()

if __name__ == "__main__":
	Main()
