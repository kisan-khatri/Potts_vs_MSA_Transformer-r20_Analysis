#!/usr/bin/env python
from mi3gpu.utils import seqload, getMarginals
import sys, argparse
import numpy as np
from numpy.random import rand

parser = argparse.ArgumentParser(description='Compute Xijab values')
parser.add_argument('msa')
parser.add_argument('q', type=int)
parser.add_argument('N', type=int)
args = parser.parse_args(sys.argv[1:])

in_msa = seqload.loadSeqs(args.msa)[0]
N, q = args.N, args.q

unimarg = getMarginals.getMarginals(in_msa, q, uni=True, bi=False)[0]
p = np.cumsum(unimarg, axis=1)
p = p/(p[:,-1][:,None]) #this is optional. correct floating-point error

seqs = np.array([np.searchsorted(pr, rand(N)) for pr in p], dtype='<u1').T

seqload.writeSeqs(sys.stdout, seqs)
