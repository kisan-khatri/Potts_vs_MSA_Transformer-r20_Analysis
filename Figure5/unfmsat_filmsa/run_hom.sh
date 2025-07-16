#!/usr/bin/env bash

# create the db for input.mi3

./HOM_r20/HOM_r20.py make_db RR 3000 filtered_input_0.5_ref.mi3 --npos 2-8 # RR reference

# compute the r20s for msa_mapped
./HOM_r20/HOM_r20.py count RR r20_MSATUF6K msa_nat.mi3 # RR MSA-T gen
./HOM_r20/HOM_r20.py count RR r20_MSATF6K msa_mappedf6k # RR msa-t 6k  gen
#./HOM_r20/HOM_r20.py count RR r20_indep output.mi3
./HOM_r20/HOM_r20.py count RR r20_ref filtered_input_0.5_nat.mi3 # RR natural

# Potts sequences obtained by running:
# bzcat fitD/run_15/seqs | head -n 73061 >seqs_generated

