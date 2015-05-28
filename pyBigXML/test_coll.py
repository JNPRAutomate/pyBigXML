#!/usr/bin/env python

import xmltodict
import pprint

d = xmltodict.parse(open("/Users/rcameron/Desktop/show_routes-27MAY2015.xml"), process_namespaces=False)
