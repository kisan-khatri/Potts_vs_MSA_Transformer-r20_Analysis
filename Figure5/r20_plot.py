import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D  # For custom legend elements

# Create a 2x2 subplot layout
fig, axs = plt.subplots(2, 2, figsize=(5.7, 5.7))

# First subplot
potts = np.load('r20_Potts.npy')
potts1 = np.nanmean(potts, axis=1)
msa = np.load('r20_MSAT.npy')
msa1 = np.nanmean(msa, axis=1)
ref = np.load('r20_ref.npy')
ref1 = np.nanmean(ref, axis=1)
indep = np.load('r20_indep.npy')
indep1 = np.nanmean(indep, axis=1)

axs[0, 0].plot(range(2, 9), potts1, '.--', color='tab:blue', zorder=100)
axs[0, 0].plot(range(2, 9), msa1, '.-', color='tab:orange')
axs[0, 0].plot(range(2, 9), indep1, '.-', color='tab:grey')
axs[0, 0].plot(range(2, 9), ref1, '.-', color='tab:green')
axs[0, 0].set_ylim(0, 1.05)
axs[0, 0].set_ylabel('r20', fontsize=13)
axs[0, 0].set_xlabel('Pattern Length', fontsize=13)
axs[0, 0].set_xticks([2, 4, 6, 8])
axs[0, 0].set_yticks([0.0, 0.5, 1.0])
axs[0, 0].tick_params(axis='both', labelsize=13)
axs[0, 0].text(0.0, 1.03, "(a)", transform=axs[0, 0].transAxes, size=13,
               verticalalignment='bottom', horizontalalignment='left',)
# Second subplot
potts = np.load('pi_f_munf/r20_Potts.npy')
potts1 = np.nanmean(potts, axis=1)
msa = np.load('pi_f_munf/r20_MSAT.npy')
msa1 = np.nanmean(msa, axis=1)
ref = np.load('pi_f_munf/r20_ref.npy')
ref1 = np.nanmean(ref, axis=1)
indep = np.load('pi_f_munf/r20_indep.npy')
indep1 = np.nanmean(indep, axis=1)

axs[0, 1].plot(range(2, 9), potts1, '.--', color='tab:blue', zorder=100)
axs[0, 1].plot(range(2, 9), msa1, '.-', color='tab:orange')
axs[0, 1].plot(range(2, 9), indep1, '.-', color='tab:grey')
axs[0, 1].plot(range(2, 9), ref1, '.-', color='tab:green')
axs[0, 1].set_ylim(0, 1.05)
axs[0, 1].set_xlabel('Pattern Length', fontsize=13)
axs[0, 1].set_xticks([2, 4, 6, 8])
axs[0, 1].set_yticks([0.0, 0.5, 1.0])
axs[0, 1].set_yticklabels(['', '', ''])
axs[0, 1].tick_params(axis='both', labelsize=13)
axs[0, 1].text(0.0, 1.03, "(b)", transform=axs[0, 1].transAxes, size=13,
               verticalalignment='bottom', horizontalalignment='left',)
# Third subplot
potts = np.load('unfmsat_filmsa/r20_MSATF6K.npy')
potts1 = np.nanmean(potts, axis=1)
msa = np.load('unfmsat_filmsa/r20_MSATUF6K.npy')
msa1 = np.nanmean(msa, axis=1)
ref = np.load('unfmsat_filmsa/r20_ref.npy')
ref1 = np.nanmean(ref, axis=1)
indep = np.load('unfmsat_filmsa/r20_indep.npy')
indep1 = np.nanmean(indep, axis=1)
p = np.load('unfmsat_filmsa/r20_Potts.npy')
p1 = np.nanmean(p, axis=1)

axs[1, 0].plot(range(2, 9), potts1, '.-', color='tab:red', zorder=100)
axs[1, 0].plot(range(2, 9), msa1, '.-', color='tab:orange')
axs[1, 0].plot(range(2, 9), p1, '.--', color='tab:blue')
axs[1, 0].plot(range(2, 9), indep1, '.-', color='tab:grey')
axs[1, 0].plot(range(2, 9), ref1, '.-', color='tab:green')
axs[1, 0].set_ylim(0, 1.05)
axs[1, 0].set_ylabel('r20', fontsize=13)
axs[1, 0].set_xlabel('Pattern Length', fontsize=13)
axs[1, 0].set_xticks([2, 4, 6, 8])
axs[1, 0].set_yticks([0.0, 0.5, 1.0])
axs[1, 0].tick_params(axis='both', labelsize=13)
axs[1, 0].text(0.0, 1.03, "(c)", transform=axs[1, 0].transAxes, size=13,
               verticalalignment='bottom', horizontalalignment='left',)
# Fourth subplot for legends only
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='tab:blue', markersize=8, label='Potts'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='tab:orange', markersize=8, label='Unfiltered MSA-T'),
 Line2D([0], [0], marker='o', color='w', markerfacecolor='tab:red', markersize=8, label='Filtered MSA-T'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='tab:grey', markersize=8, label='Indep'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='tab:green', markersize=8, label='Null Model')
]
axs[1, 1].legend(handles=legend_elements, loc='center', fontsize=10, frameon=False)
axs[1, 1].axis('off')  # Turn off axis for clean legend display

plt.tight_layout(pad=1.02)
plt.show()

