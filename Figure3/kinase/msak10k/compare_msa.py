import numpy as np
from mi3gpu.utils import seqload
from mi3gpu.utils.getMarginals import getMarginals
import sys

msa1name = sys.argv[1]
msa2name = sys.argv[2]

msa1 = seqload.loadSeqs(msa1name)[0]
msa2 = seqload.loadSeqs(msa2name)[0]
print(msa1.shape, msa2.shape)
print(msa1[0], msa2[0])
assert(msa1.shape == msa2.shape)
assert(all((msa1==msa2).flatten()))
print('{} and {} are identical'.format(msa1name, msa2name))
