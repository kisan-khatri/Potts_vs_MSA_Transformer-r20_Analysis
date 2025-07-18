There are 4 plots in Figure 4. First two for r20 and last two for cc-r20. All you need to run is :
python r20_plot.py (to directly reproduce Figure 4). Since, sequence files with 6M sequences were solarge, and I am unable to upload those files at the moment in GitHub. However, you can find those files from Zenodo.

	Note: this is the plot with MSAs containing 6M sequences each. So, they are of very large sizes and I am unable to upload in GitHuB directly those sequence files. However, I have put all the estimated r20 file (.npy files) for each of them to reproduce our plots. For how to generate 6M sequences, you can simply use the idea from Figure3/readme.md. Thank you.

#You can follow all the ideas from figure 3. Since, figure 4 is based on all 6M sequences, we have very large data files. So, I have only provided sequence MSA files, and necessary .npy file to reproduce figure 4. If you want to generate, take idea from file "Figure3".

#Please see the GitHub link how we generate synthetic sequences using the Potts model and MSA Transformer. For the Independent model, run the following command in the Mi3-GPU environment where you work for the Potts model:

python gen_indep.py input_MSA.mi3 output.mi3 #gen_indep.py: keep this in your working directory

#install Mi3-GPU and other necessary packages.

Keep this in the current directory: HOM_r20.py

#the script you need to run is:
sbatch run_hom.sh 

 It creates RR.db file for reference MSA. Then we compute r20 for all the generated MSAs against reference MSA. It creates following files:
r20_Potts.npy - for potts
r20_MSAT.npy -  for MSA-T
r20_indep.npy - for independent
r20_ref.npy - for null model.

Then for cc-r20, we use previously created RR.db and proceed further to run:
'sbatch run_hom_cc.sh', which produce RR_cc.db for reference MSA, finally  which will give 4 files for cc-r20 as:

r20_potts_cc.npy - for potts
r20_MSAT_cc.npy -  for MSA-T
r20_indep_cc.npy - for independent
r20_ref_cc.npy - for null model.


You should be able to run now the final script:

python r20_plot.py which will reproduce the Figure 4 of our manuscript.
All necessary files are provided.
