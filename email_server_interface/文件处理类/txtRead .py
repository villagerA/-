import codecs
import sys

fname = fname = raw_input('Enter a file name Make sure the file is in the current directory with the .xls suffix:')

str1= '#!/bin/bash (echo "Content-Type: text/html";cat mail.txt)|/usr/sbin/sendmail'
f = open(fname)
for i in f:
	str1= str1+' -c ' + i.strip()

print str1