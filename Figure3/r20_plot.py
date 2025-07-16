import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D  # Import for custom legend lines

plt.figure(figsize=(6, 3))  # Adjusted to make x and y axes proportional

# First subplot
potts = np.load('RR_6K_NAT_REF/r20_Potts.npy')
potts1 = np.nanmean(potts, axis=1)
msa = np.load('RR_6K_NAT_REF/r20_MSAT.npy')
msa1 = np.nanmean(msa, axis=1)
ref = np.load('RR_6K_NAT_REF/r20_ref.npy')
ref1 = np.nanmean(ref, axis=1)
indep = np.load('RR_6K_NAT_REF/r20_indep.npy')
indep1 = np.nanmean(indep, axis=1)

plt.subplot(121)  # Changed from 131 to 121 (only 2 subplots)
plt.plot(range(2, 9), potts1, '.--', color='tab:blue', zorder=100)
plt.plot(range(2, 9), msa1, '.-', color='tab:orange')
plt.plot(range(2, 9), indep1, '.-', color='tab:grey')
plt.plot(range(2, 9), ref1, '.-', color='tab:green')
plt.ylim(0, 1.05)
plt.ylabel('r20', fontsize=13)
plt.xlabel('Pattern Length', fontsize=13)

# Custom legend with small balls
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='tab:blue', markersize=8, label='Potts'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='tab:orange', markersize=8, label='MSA-T'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='tab:grey', markersize=8, label='Indep'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='tab:green', markersize=8, label='Null Model')
]
plt.legend(handles=legend_elements, loc='lower left', fontsize=9, frameon=False)

plt.xticks(ticks=[2, 4, 6, 8], fontsize=13)
plt.yticks(ticks=[0.0, 0.5, 1.0], fontsize=13)

# Second subplot
plt.subplot(122)  # Changed from 132 to 122
potts = np.load('kinase/msak10k/r20_Potts_new.npy')
potts1 = np.nanmean(potts, axis=1)
msa = np.load('kinase/msak10k/r20_MSAT_new.npy')
msa1 = np.nanmean(msa, axis=1)
ref = np.load('kinase/msak10k/r20_ref_new.npy')
ref1 = np.nanmean(ref, axis=1)
indep = np.load('kinase/msak10k/r20_indep.npy')
indep1 = np.nanmean(indep, axis=1)
plt.plot(range(2, 9), potts1, '.--', color='tab:blue', zorder=100)
plt.plot(range(2, 9), msa1, '.-', color='tab:orange')
plt.plot(range(2, 9), indep1, '.-', color='tab:grey')
plt.plot(range(2, 9), ref1, '.-', color='tab:green')
plt.ylim(0, 1.05)
plt.xlabel('Pattern Length', fontsize=13)

plt.xticks(ticks=[2, 4, 6, 8], fontsize=13)
plt.yticks(ticks=[0.0, 0.5, 1.0], labels=['', '', ''])

plt.tight_layout(pad=1.2)  # Ensuring proper layout
plt.show()
