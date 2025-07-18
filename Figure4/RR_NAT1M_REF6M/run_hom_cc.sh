#!/usr/bin/env bash
#SBATCH --job-name=r20_p
#SBATCH --partition=normal
#SBATCH --exclusive
#SBATCH --nodes=1
#SBATCH --time=10:00:00
#SBATCH --output=stdout
#SBATCH --error=stderr

# create the db for input.mi3
#./HOM_r20/HOM_r20.py make_db RR 3000 Pottsref/seqs --npos 2-8 # Potts Ref
./HOM_r20/HOM_r20.py convert_cc_db RR.db RR_cc Pottsref/seqs --cutoff 6 # Potts Ref

# compute the r20s for msa_mapped
#./HOM_r20/HOM_r20.py count RR r20_MSAT msa_combined # RR MSA-T gen
./HOM_r20/HOM_r20.py count_cc RR_cc r20_MSAT_cc msa_combined # RR MSA-T gen
./HOM_r20/HOM_r20.py count_cc RR_cc r20_potts_cc Potts/genA/seqs # RR Potts gen
./HOM_r20/HOM_r20.py count_cc RR_cc r20_indep_cc independentmodel/output.mi3 # RR Indep gen
./HOM_r20/HOM_r20.py count_cc RR_cc r20_ref_cc Pottsref/Potts/genB/seqs #nat

# Potts sequences obtained by running:
# bzcat fitD/run_15/seqs | head -n 73061 >seqs_generated

