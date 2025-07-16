#!/usr/bin/env python

with open('filtered_input_0.5_nat.mi3') as f:
    seqs = f.readlines()

with open('filtered_input_0.5_nat.fasta', 'wt') as f:
    for s in seqs:
        print("> seqname", file=f)
        print(s.strip(), file=f)
