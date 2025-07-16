#!/usr/bin/env python
from glob import glob
import numpy as np
import pickle
# combine all new tokens together
n = 0
for filename in sorted(glob('RR_*/*/new-tokens.npy')):
    print(filename)
    x = np.load(filename)
    x = x.reshape(x.shape[1], 233)
    if n == 0:
        msa = x
    else:
        msa2 = x
        msa = np.vstack([msa, msa2])
    n += 1

print(msa)
print(msa.shape)
print(msa[-1])
with open('dictionary-tokens.pkl', 'rb') as f:
    data= pickle.load(f)
print(data)
data2 = {b:a for a,b in data.items()}
msa_mapped = np.array(["".join([data2[s] for s in seq[1:]]) for seq in msa])


with open('msa_mapped', 'w') as f:
    for line in msa_mapped:
        f.write(line + '\n')

print(msa_mapped)
print(msa_mapped.shape, msa_mapped.dtype)

