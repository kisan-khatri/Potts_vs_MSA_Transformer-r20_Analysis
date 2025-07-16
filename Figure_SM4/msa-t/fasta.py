#!/usr/bin/env python

with open('msa_mapped') as f:
    seqs = f.readlines()

with open('msa_mapped.fasta', 'wt') as f:
    for s in seqs:
        print("> seqname", file=f)
        print(s.strip(), file=f)
