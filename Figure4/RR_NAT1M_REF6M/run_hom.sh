#!/usr/bin/env bash
#SBATCH --job-name=r20_p
#SBATCH --partition=normal
#SBATCH --exclusive
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --output=stdout
#SBATCH --error=stderr

# create the db for input.mi3
#./HOM_r20/HOM_r20.py make_db RR 3000 Pottsref/seqs --npos 2-8 # Potts Ref
./HOM_r20/HOM_r20.py make_db RR 3000 Pottsref/seqs --npos 2-8 # Potts Ref

# compute the r20s for msa_mapped
#./HOM_r20/HOM_r20.py count RR r20_MSAT msa_combined # RR MSA-T gen
./HOM_r20/HOM_r20.py count RR r20_MSAT msa_combined # RR MSA-T gen
./HOM_r20/HOM_r20.py count RR r20_Potts Potts/genA/seqs # RR Potts gen
./HOM_r20/HOM_r20.py count RR r20_indep independentmodel/output.mi3 # RR Indep gen
./HOM_r20/HOM_r20.py count RR r20_ref Pottsref/Potts/genB/seqs #nat

# Potts sequences obtained by running:
# bzcat fitD/run_15/seqs | head -n 73061 >seqs_generated

