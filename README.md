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
