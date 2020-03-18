#!/usr/bin/env python3

from itertools import groupby
import sys

def iter_hits(hits):
    for i in range(1,len(hits)):
        (p, c) = hits[i-1], hits[i]
        yield p, c

def is_overlap(hits):
    for p, c in iter_hits(hits):
        if c[5] < p[6]:
            return True

def is_nonoverlap(hits):
    for p, c in iter_hits(hits):
        if c[5] > p[6]:
            return True



fh = open(sys.argv[1])
fh.next()
oh1 = open('mixed1.txt', 'w')
oh2 = open('overlaps-blast.txt', 'w')
oh3 = open('nonoverlaps1.txt', 'w')

for qid, grp in groupby(fh, lambda l: l.split()[0]):
    hits = []
    for line in grp:
        hsp = line.split()
        hsp[5], hsp[6] = int(hsp[5]), int(hsp[6])
        hits.append(hsp)
    hits.sort(key=lambda x: x[5])
    if len(hits)==1:
        oh = oh3
    elif is_nonoverlap(hits):
        oh = oh3
        if is_overlap(hits):
            oh = oh1
    else:
        oh = oh2

    for hit in hits:
        oh.write('\t'.join([str(f) for f in hit])+'\n')