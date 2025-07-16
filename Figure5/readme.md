There are 3 plots in Figure 5.
#Please see the GitHub link how we generate synthetic sequences using the Potts model and MSA Transformer. For the Independent model, run the following command in the Mi3-GPU environment where you work for the Potts model:

python gen_indep.py input_MSA.mi3 output.mi3 #gen_indep.py: keep this in your working directory

#install Mi3-GPU and other necessary packages.

Keep this in the current directory: HOM_r20.py

1. The first plot is for all 30k natural unfiltered data (special filtering-see methods in the manuscript)

#the script you need to run is:
sbatch run_hom.sh 

 It creates RR.db file for reference MSA. Then we compute r20 for all the generated MSAs against reference MSA. It creates following files:
r20_Potts.npy - for potts
r20_MSAT.npy -  for MSA-T
r20_indep.npy - for independent
r20_ref.npy - for null model.

2. In the second plot, the potts and independent model are trained on 6K fltered natural MSA, MSA-T was trained on 30K unfiltered MSA, and the reference MSA is unfiltered MSA with 30K sequences.

the script run_hom.sh should be run for all 3 different cases independently, which gives corresponding r20 metric for each models as I have provided above for each models. The necessary files for 2nd plot are in the directory 

"pi_f_munf".

3. The third plot is for same for all the models, evaluated against 6K filtered natural sequences. All the necessary files are in the directory:
  "unfmsat_filmsa"

Please see corresponding "run_hom.sh" file to see which MSA contains what kind of MSA and with how many sequences (filtered 6K or unfiltered 30K).

You should be able to run now the final script:

python r20_plot.py which will reproduce the Figure 5 of our manuscript.

