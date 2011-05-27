#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import gv
import re


def filter_cont(s):
	s = s.replace("(  ", "(")
	s = s.replace("  ", ",")
	s = s.replace(")\r", ")")
	s = s.replace(") ", ")")
	return s

ls = []
lt = []
ds = {}
f = open("prak2_aufg2 Erreichbarkeitsgraph.txt", "r")
r1 = re.compile("^(.+)---(.+)---> (.+)")
r2 = re.compile("(.+):\s+\d+ (.+)")
for line in f:
	m1 = r1.match(line)
	if not m1:
		# end of file or error..
		#print line,
		break
	s1 = m1.group(1)
	m2 = r2.match(s1)
	if m2:
		s1_name = m2.group(1)
		s1_cont = filter_cont(m2.group(2))
		if not s1_cont in ls:
			ls.append(s1_cont)
			ds[s1_name] = s1_cont

	s2 = m1.group(3)
	m2 = r2.match(s2)
	s2_name = m2.group(1)
	s2_cont = filter_cont(m2.group(2))
	if not s2_cont in ls:
		ls.append(s2_cont)
		ds[s2_name] = s2_cont

	t = m1.group(2)
	lt.append((s1_cont, s2_cont, t))

G = gv.graph("G")
N = gv.protonode(G)
E = gv.protoedge(G)
gv.setv(N, 'shape', 'box')

dNodes = {}
for node in ls:
	name = node
	dNodes[name] = gv.node(G, name)

for k in lt:
	edge = gv.edge(dNodes[k[0]], dNodes[k[1]])
	gv.setv(edge, 'label', k[2])
	gv.setv(edge, 'dir', "forward")

gv.layout(G, 'dot')
#gv.render(G, 'xlib')
gv.render(G, 'pdf', "eg.pdf")
