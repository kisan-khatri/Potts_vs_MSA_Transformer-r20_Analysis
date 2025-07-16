import numpy as np
import matplotlib.pyplot as plt
from scipy.special import entr

# Load univariate marginals (shape: [L, 21])
train_uni = np.load("nat_training/train_uni.npy")
potts_uni = np.load("potts/potts_uni.npy")
msa_t_uni = np.load("msa-t/msa_t_uni.npy")
indep_uni = np.load("indep/indep_uni.npy")

# Compute entropy across the 21 possible characters (including gap)
entropy_train = np.sum(entr(train_uni)/np.log(2), axis=1)
entropy_potts = np.sum(entr(potts_uni)/np.log(2), axis=1)
entropy_msat  = np.sum(entr(msa_t_uni)/np.log(2), axis=1)
entropy_indep = np.sum(entr(indep_uni)/np.log(2), axis=1)

# Optional: conservation score = 1 / entropy
epsilon = 1e-8  # to avoid division by zero
conservation_train = 1 / (entropy_train + epsilon)
conservation_potts = 1 / (entropy_potts + epsilon)
conservation_msat  = 1 / (entropy_msat + epsilon)
conservation_indep = 1 / (entropy_indep + epsilon)

# === Plotting Entropy ===
plt.figure(figsize=(12, 5))
plt.plot(entropy_train, label="Training", color="black", linewidth=2)
plt.plot(entropy_potts, label="Potts", color="blue")
plt.plot(entropy_msat, label="MSA-T", color="green")
plt.plot(entropy_indep, label="Independent", color="orange")

plt.xlabel("MSA Position")
plt.ylabel("Entropy (bits)")
plt.title("Per-Position Entropy")
plt.legend()
plt.tight_layout()
plt.savefig("entropy_with gap.png", dpi=300)
plt.show()

# === Plotting Conservation ===
plt.figure(figsize=(12, 5))
plt.plot(conservation_train, label="Training", color="black", linewidth=2)
plt.plot(conservation_potts, label="Potts", color="blue")
plt.plot(conservation_msat, label="MSA-T", color="green")
plt.plot(conservation_indep, label="Independent", color="orange")

plt.xlabel("MSA Position")
plt.ylabel("Conservation Score (1 / Entropy)")
plt.title("Per-Position Conservation")
plt.legend()
plt.tight_layout()
plt.savefig("conservation_acore.png", dpi=300)
plt.show()
