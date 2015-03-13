#Documentation

# Introduction #
Ever needed to know what the f@@@ some internet slang word means if you're a internet beginner.
Now you can.

# Details #
My program currently supports:
  * Searching in a small dictionary for words that You input in the Entry box.
  * Lists them in a TreeView.
  * The program has a button to clear the results list.


# unofficial fileList2dic guide #
To make a new dictionary, manually copy two column list, key and values:
e.g> brb be right back
but you need somehow with a help of a regex to make tabs between each key and value.
in Gedit or Notepad++ that can be done like this>
pressing control + h pops a replace dialog, one must copy and paste> the space between the key and values, then in Replace with to enter \t.
After that just save the file and name it as islang\_all, than it shall generate a dictionary file named "slang.dic", be careful, backup any existing files before running it.
Copy or move the "slang.dic" file to your home folder (GNU/Linux: home directory, windows: My documents) then in the folder .islanger.
The current version has untested cli version, please don't report a bug about the dictionary, because I haven't figure the code yet.

## Soon ##
Graphical dictionary editor.
Complete codes are welcomed, preferable if the code is> core and gui, not hard coded gui.