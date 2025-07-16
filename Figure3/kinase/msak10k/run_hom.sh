#!/usr/bin/env bash

# create the db for input.mi3

./HOM_r20/HOM_r20.py make_db RR 1000 nat_filt_0.5_10K_ref --npos 2-8 # RR natural

# compute the r20s for msa_mapped
#./HOM_r20/HOM_r20.py count RR r20_MSAT msa_mapped # RR MSA-T gen
#./HOM_r20/HOM_r20.py count RR r20_Potts seqs_generated # RR Potts gen
./HOM_r20/HOM_r20.py count RR r20_indep output.mi3

# Potts sequences obtained by running:
# bzcat fitD/run_15/seqs | head -n 73061 >seqs_generated

