#!/usr/bin/env bash
#SBATCH --job-name=MSA_Trans
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --gpus=2
#SBATCH --ntasks-per-node=1
#SBATCH --mem=2G
#SBATCH --time=48:00:00
#SBATCH --output=stdout
#SBATCH --error=stderr

for r in msas/RR_{000..016}
do
	nseq=$(grep -c '>' $r)
	python core.py --Iters 200 --filename $r --num $nseq --depth 1 --new_dir output/$r --filepath $PWD
done
