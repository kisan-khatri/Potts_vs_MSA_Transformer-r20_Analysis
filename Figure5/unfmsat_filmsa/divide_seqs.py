import numpy as np
import sys,os

filename = str(sys.argv[1])
N1 = int(sys.argv[2])
N2 = int(sys.argv[3])

seqs = []

with open(filename, 'r') as f:
    for seq in f.readlines():
        seqs.append(seq.strip())

seqs = np.array(seqs)

np.random.shuffle(seqs)

with open('msa_ref.mi3', 'w') as f:
    for seq in seqs[:N1]:
        print(seq, file=f)

with open('msa_nat.mi3', 'w') as f:
    for seq in seqs[N1:N1+N2]:
        print(seq, file=f)

#with open('filtered_input_0.5_nat.fasta', 'w') as f:
    #for seq in seqs[N1:N1+N2]:
     #   seq = "> seqname\n"+seq
      #  print(seq, file=f)

