#!/usr/bin/env python

with open('seqs_generated') as f:
    seqs = f.readlines()

with open('seqs_generated.fasta', 'wt') as f:
    for s in seqs:
        print("> seqname", file=f)
        print(s.strip(), file=f)
