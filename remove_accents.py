#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  Copyright 2019 Dimitris Tzemos <dijemos@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
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
	sys.exit(main(sys.argv))
