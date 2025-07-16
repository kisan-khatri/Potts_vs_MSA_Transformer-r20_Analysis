#!/usr/bin/env bash

# create the db for nat_filt_0.5_10K_train
./HOM_r20/HOM_r20.py make_db RR 3000 nat_filt_0.5_10K_ref --npos 2-8

# compute the r20s for msa_mapped
./HOM_r20/HOM_r20.py count RR kinase r20_MSAT_new output/msas/msa_mapped
./HOM_r20/HOM_r20.py count RR kinase r20_Potts_new ../pottsk10k/gen10k
./HOM_r20/HOM_r20.py count RR kinase r20_ref_new ../pottsk10k/nat_filt_0.5_10K_train
./HOM_r20/HOM_r20.py count RR r20_indep output.mi3
