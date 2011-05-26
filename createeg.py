#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import gv
import re

ls = []
dt = []
f = open("prak2_aufg2 Erreichbarkeitsgraph.txt", "r")
r1 = re.compile("^(.+)---(.+)--->(.+)")
r2 = re.compile("(.+):\s+\d+ (.+)")
for line in f:
	m1 = r1.match(line)
	if not m1:
		# end of file or error..
		break
	s1 = m1.group(1)
	m2 = r2.match(s1)
	if m2:
		s1_name = m2.group(1)
		s1_cont = m2.group(2)
		if not s1_name in ls:
			ls.append(s1_name)

	s2 = m1.group(3)
	m2 = r2.match(s2)
	s2_name = m2.group(1)
	s2_cont = m2.group(2)
	if not s2_name in ls:
		ls.append(s2_name)

	t = m1.group(2)
	dt.append((s1_name, s2_name, t))

G = gv.graph("G")

dNodes = {}
for node in ls:
	dNodes[node] = gv.node(G, node)

for k in dt:
	edge = gv.edge(dNodes[k[0]], dNodes[k[1]])
	gv.setv(edge, 'label', k[2])
	gv.setv(edge, 'dir', "forward")

gv.layout(G, 'twopi')
#gv.render(G, 'xlib')
gv.render(G, 'pdf', "eg.pdf")
