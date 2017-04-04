#! /usr/bin/env python

from Morse import *
import sys

if len(sys.argv) >= 2:
	r = Morse(26)
	g = Morse(21)
	b = Morse(20)
	w = Morse(19)
	r.write_string(sys.argv[1])
	g.write_string(sys.argv[1])
	b.write_string(sys.argv[1])
	w.write_string(sys.argv[1])
