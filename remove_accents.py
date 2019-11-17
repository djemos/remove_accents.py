#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")
import re
import unicodedata

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
        
def main(args):
	coding1 = "utf-8"
	if len(sys.argv) >=3:
		f= open(sys.argv[1], 'rb')
		text= unicode(f.read(), coding1)
		f.close()

		f= open(sys.argv[2], 'wb')
		f.write(strip_accents(text))
		f.close()
	else:
		#Δοκιμή
		text=unicode("Ὦ κοινὸν αὐτάδελφον Ἰσμήνης κάρα,")
		print(strip_accents(text))
    

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
