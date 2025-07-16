#!/usr/bin/env python

with open('output.mi3') as f:
    seqs = f.readlines()

with open('output.fasta', 'wt') as f:
    for s in seqs:
        print("> seqname", file=f)
        print(s.strip(), file=f)
