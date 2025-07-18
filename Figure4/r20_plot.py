import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D  # For custom legend elements

fig, axs = plt.subplots(2, 2, figsize=(5.7, 5.7))  # Creating a 2x2 subplot layout

# Plot 1 (Top-Left)
potts1 = np.nanmean(np.load('RR_NAT1M_REF6M/r20_Potts.npy'), axis=1)
msa1 = np.nanmean(np.load('RR_NAT1M_REF6M/r20_MSAT.npy'), axis=1)
indep1 = np.nanmean(np.load('RR_NAT1M_REF6M/r20_indep.npy'), axis=1)
ref1 = np.nanmean(np.load('RR_NAT1M_REF6M/r20_ref.npy'), axis=1)
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

# Custom legend for the first plot
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='tab:blue', markersize=8, label='Potts'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='tab:orange', markersize=8, label='MSA-T'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='tab:grey', markersize=8, label='Indep'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='tab:green', markersize=8, label='Null Model')
]
axs[0, 0].legend(handles=legend_elements, loc='lower left', fontsize=10, frameon=False)
axs[0, 0].text(0.0, 1.03, "(a)", transform=axs[0, 0].transAxes, size=13,
               verticalalignment='bottom', horizontalalignment='left',)

# Plot 2 (Top-Right)
potts2 = np.nanmean(np.load('synthetic_RR_MSA_T/r20_Potts.npy'), axis=1)
msa2 = np.nanmean(np.load('synthetic_RR_MSA_T/r20_MSAT.npy'), axis=1)
indep2 = np.nanmean(np.load('synthetic_RR_MSA_T/r20_indep.npy'), axis=1)
ref2 = np.nanmean(np.load('synthetic_RR_MSA_T/r20_ref.npy'), axis=1)
axs[0, 1].plot(range(2, 9), potts2, '.--', color='tab:blue', zorder=100)
axs[0, 1].plot(range(2, 9), msa2, '.-', color='tab:orange')
axs[0, 1].plot(range(2, 9), indep2, '.-', color='tab:grey')
axs[0, 1].plot(range(2, 9), ref2, '.-', color='tab:green')
axs[0, 1].set_ylim(0, 1.05)
axs[0, 1].set_xlabel('Pattern Length', fontsize=13)
axs[0, 1].set_xticks([2, 4, 6, 8])
axs[0, 1].set_yticks([0.0, 0.5, 1.0])
axs[0, 1].set_yticklabels([])  # Remove y-axis tick labels
axs[0, 1].tick_params(axis='x', labelsize=13)
axs[0, 1].text(0.0, 1.03, "(b)", transform=axs[0, 1].transAxes, size=13,
               verticalalignment='bottom', horizontalalignment='left',)

# Plot 3 (Bottom-Left)
potts3 = np.nanmean(np.load('RR_NAT1M_REF6M/r20_potts_cc.npy'), axis=1)
msa3 = np.nanmean(np.load('RR_NAT1M_REF6M/r20_MSAT_cc.npy'), axis=1)
indep3 = np.nanmean(np.load('RR_NAT1M_REF6M/r20_indep_cc.npy'), axis=1)
ref3 = np.nanmean(np.load('RR_NAT1M_REF6M/r20_ref_cc.npy'), axis=1)
axs[1, 0].plot(range(2, 7), potts3, '.--', color='tab:blue', zorder=100)
axs[1, 0].plot(range(2, 7), msa3, '.-', color='tab:orange')
axs[1, 0].plot(range(2, 7), indep3, '.-', color='tab:grey')
axs[1, 0].plot(range(2, 7), ref3, '.-', color='tab:green')
axs[1, 0].set_ylim(0, 1.05)
axs[1, 0].set_ylabel('cc-r20', fontsize=13)
axs[1, 0].set_xlabel('Pattern Length', fontsize=13)
axs[1, 0].set_xticks([2, 4, 6])
axs[1, 0].set_yticks([0.0, 0.5, 1.0])
axs[1, 0].tick_params(axis='both', labelsize=13)
axs[1, 0].text(0.0, 1.03, "(c)", transform=axs[1, 0].transAxes, size=13,
               verticalalignment='bottom', horizontalalignment='left',)

# Plot 4 (Bottom-Right)
potts4 = np.nanmean(np.load('synthetic_RR_MSA_T/r20_potts_cc.npy'), axis=1)
msa4 = np.nanmean(np.load('synthetic_RR_MSA_T/r20_MSAT_cc.npy'), axis=1)
indep4 = np.nanmean(np.load('synthetic_RR_MSA_T/r20_indep_cc.npy'), axis=1)
ref4 = np.nanmean(np.load('synthetic_RR_MSA_T/r20_ref_cc.npy'), axis=1)
axs[1, 1].plot(range(2, 7), potts4, '.--', color='tab:blue', zorder=100)
axs[1, 1].plot(range(2, 7), msa4, '.-', color='tab:orange')
axs[1, 1].plot(range(2, 7), indep4, '.-', color='tab:grey')
axs[1, 1].plot(range(2, 7), ref4, '.-', color='tab:green')
axs[1, 1].set_ylim(0, 1.05)
axs[1, 1].set_xlabel('Pattern Length', fontsize=13)
axs[1, 1].set_xticks([2, 4, 6])
axs[1, 1].set_yticks([0.0, 0.5, 1.0])
axs[1, 1].set_yticklabels([])  # Remove y-axis tick labels for bottom-right
axs[1, 1].tick_params(axis='x', labelsize=13)
axs[1, 1].text(0.0, 1.03, "(d)", transform=axs[1, 1].transAxes, size=13,
               verticalalignment='bottom', horizontalalignment='left',)

# Adjust layout and show
plt.tight_layout(pad=1.02)
plt.show()

