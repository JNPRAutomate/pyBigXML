#!usr/bin/env python

from pyBigXML import pyBigXML

pbx = pyBigXML("test.xml")
o = pbx.parse()
print o
