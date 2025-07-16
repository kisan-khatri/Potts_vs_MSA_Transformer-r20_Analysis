#!/usr/bin/env python
from random import shuffle
from itertools import groupby

# load sequences
with open('10ktrain.fa') as f:
    lines = [l.strip() for l in f]
seqs = ["".join(v) for k,v in 
        groupby(lines, lambda x: x.startswith('>')) if not k]

with open('input.mi3', 'wt') as f:
    f.write("\n".join(seqs))

# randomize sequence order
shuffle(seqs)

# divide seqs into chunks of size 600
chunks = [seqs[600*i:600*i+600] for i in range(len(seqs)//600 + 1)]

# write each chunk to a separate file
for n,chunk in enumerate(chunks):
    with open(f'msas/RR_{n:03d}', 'wt') as f:
        for seq in chunk:
            f.write("> x\n")
            f.write(seq + '\n')

# print out chunk sizes
with open('chunksizes', 'wt') as f:
    print(" ".join(str(len(c)) for c in chunks), file=f)

