#!/usr/bin/env bash

# create the db for reference MSA

./HOM_r20/HOM_r20.py make_db RR 3000 ref30k --npos 2-8 # RR reference 30k

# compute the r20s for msa_mapped
./HOM_r20/HOM_r20.py count RR r20_MSAT msa_mapped # RR MSA-T gen 30k
./HOM_r20/HOM_r20.py count RR r20_Potts seqs_generated # RR Potts gen 30k
./HOM_r20/HOM_r20.py count RR r20_indep output.mi3 #Indep gen 3ok
./HOM_r20/HOM_r20.py count RR r20_ref nat30k #RR nat 30k


