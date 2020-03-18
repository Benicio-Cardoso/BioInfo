#!/bin/python

import collections
import os


Nucleotides = ['A', 'C', 'T', 'G']

def validseq(seq):
	tmpseq = seq.upper()
	for nucl in tmpseq:
		if nucl not in Nucleotides:
			return false
		return tmpseq

def countnuclfreq(seq):
	tmpfreqdict = {"a":0, "c":0, "t":0, "g":0}
	for nucl in seq:
		tmpfreqdict[nucl] += 1
	return tmpfreqdict

dnastring = "atcgatcgatgca"
result = countnuclfreq(dnastring)

def countbases(seq):
	seq = seq.upper()
	dnadict={'A':0, 'T':0, 'C':0, 'G':0}
	for base in seq:
		dnadict[base] +=1
	return dnadict

dna = 'atcgatcgatcgtagtagctagcaatcgatcgatgcta'
dnadic = countbases(dna)

for nucl, countnum in dnadic.items():
	print nucl, countnum


