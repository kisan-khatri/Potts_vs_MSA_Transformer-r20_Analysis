# Phylogenetic Corrections and Higher-Order Sequence Statistics in Protein Families: The Potts Model vs MSA Transformer

DOI: https://doi.org/10.48550/arXiv.2503.00289
This repository contains the code and data used in our study on double mutant cycle (cooperativity) analysis in kinase proteins, as presented in the manuscript. It includes the code to reproduce the histogram shown in the manuscript and to identify the most cooperative double mutant pairs reported. The repository is shared in response to reviewer requests to promote transparency and reproducibility. 

We present a comparative analysis of the Potts model and the MSA Transformer (MSA-T) using r20 metrics for two protein families: RR domain and kinase. For detailed methodology and results, please refer to the associated article.

# How to cite this code
If you think this has contributed to the work you are doing, consider citing it in the list of your references. Here is the recommended citation:

Khatri, K., Haldane, A., & Levy, R. M. (2025). kisan-khatri/Potts-Model-Cooperativity: v1.0.0 (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.15856333

Zenodo. https://doi.org/10.5281/zenodo.15856333
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15856333.svg)](https://doi.org/10.5281/zenodo.15856333)

# Step 1: Software Used
We used the Mi3-GPU software package to generate the synthetic sequences from the Potts model in our study which is publicly accessible via its GitHub repository: https://github.com/ahaldane/Mi3-GPU. To generate the synthetic sequences using MSA-T, we used the publicly available package via GitHub repository: https://github.com/Bitbol-Lab/Iterative_masking, which is also available at: https://doi.org/10.5281/zenodo.7684052.

# Step 2: Detailed Description of the Further Steps
For two proteins, RR Domain (PF00072) and Kinase (PF00069), we first constructed MSAs and used step 1 to generate the synthetic sequences from the Potts model and the MSA-T (Please see details in the methodology section of our manuscript). To calculate the r20 scores corresponding to the Higher Order Marginals (HOMs), and to reproduce the r20-plots as well as other supporting information reported in the manuscript and in the Supplemental Material (SM), we then followed the following steps:


# Step 2: Figure 3: r20_Plot
This is the case of 50% phylogenetically filtered MSAs for both the proteins (See manuscript for details). We trained three models, the Potts model, MSA-T, and the Independent model, to generate synthetic sequences. See details inside folder Figure3 and read readme.md inside that folder.
