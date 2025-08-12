There are 2 plots in Figure 3. The first plots is for RR domain and second is for Kinase. This is the case of filtered MSA. Please see the article for details.

#Please see the GitHub link how we generate synthetic sequences using the Potts model and MSA Transformer. For the Independent model, run the following command in the Mi3-GPU environment where you work for the Potts model:

python gen_indep.py input_MSA.mi3 output.mi3 #gen_indep.py: keep this in your working directory

#install Mi3-GPU and other necessary packages.

Keep this in the current directory: HOM_r20.py

1. The first plot is for RR domain MSA with filtered 6K sequences. All you need to do is:

 "python r20_plot.py"

#for this you first need to run the following script:
sbatch run_hom.sh 

 It creates RR.db file for reference MSA along with 'npy' files for each model. There are MSAs (reference, training, and model-generated) from which we need to compute '.npy' files for each model. Then we use those '.npy' files to compute r20 for all the generated MSAs against the reference MSA. It creates the following files:
r20_Potts.npy - for potts
r20_MSAT.npy -  for MSA-T
r20_indep.npy - for independent
r20_ref.npy - for null model.

 The necessary files for 2nd plot are in the directory

"RR_6K_NAT_REF"


2. The second plot is for Kinase MSA with filtered 10K sequences.

the script run_hom.sh should be run for both 2 different cases independently, which gives corresponding r20 metric for each models as I have provided above for each models. The necessary files for 2nd plot are in the directory 

"kinase"


Please see corresponding "run_hom.sh" file to see which MSA contains what kind of MSA and with how many sequences (filtered 6K or filtered 10K for respective proteins).

You should be able to run now the final script:

python r20_plot.py which will reproduce the Figure 3 of our manuscript.

