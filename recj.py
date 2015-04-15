#!/usr/bin/python

import sys
mapping = dict()
cjchar = list()

#f = open("cj543.cin", "r")
f = open("cj.cin", "r")
while True:
    line = f.readline()
    if len(line) == 0:
        break;

    line = line.strip()
    if line.startswith("#") or line.startswith("%"):
        #print line
        continue

    raw = line.split(" ")
    if len(raw) < 2:
        continue

    (seq, key) = raw
    #print "%s %s %d" % (key, seq, len(raw))
    if len(raw) != 2:
        print line

    mapping[key] = seq
f.close()

f = open("cj.char", "r")
while True:
    line = f.readline()
    if len(line) == 0:
        break;
    cjchar.append(line.strip())
f.close()

def decoded_to_string(d):
    out = ""
    for c in d:
        idx = ord(c) - ord('a')
        if idx < 26:
            out += "%s(%s) " % (cjchar[idx], c)
        else:
            out += "X "
    return out

if len(sys.argv) <= 1:
    print "Usage: ./cj_reverse.py <X>"
elif len(sys.argv) > 1:
    idx = sys.argv[1]
    if idx in mapping.keys():
        print "found: %s => %s" % (idx, decoded_to_string(mapping[idx]))
    else:
        print "not found : %s" % idx
