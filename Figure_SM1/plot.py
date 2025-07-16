import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from mi3gpu.utils import indepF

def load_and_correct(x_file, y_file):
    x_raw = np.load(x_file)
    y_raw = np.load(y_file)
    x_corr = x_raw - indepF(x_raw)
    y_corr = y_raw - indepF(y_raw)
    x = np.ravel(x_corr)
    y = np.ravel(y_corr)
    r, _ = pearsonr(x, y)
    return x, y, r

x_potts, y_potts, r_potts = load_and_correct('ref.npy', 'potts.npy')
x_msat, y_msat, r_msat = load_and_correct('ref.npy', 'msat.npy')
x_null, y_null, r_null = load_and_correct('nat.npy', 'ref.npy')

min_val = min(np.min(np.concatenate([x_potts, x_msat, x_null])), 
              np.min(np.concatenate([y_potts, y_msat, y_null])))
max_val = max(np.max(np.concatenate([x_potts, x_msat, x_null])), 
              np.max(np.concatenate([y_potts, y_msat, y_null])))

plt.figure(figsize=(8, 3))

# (a) Potts
plt.subplot(1, 3, 1)
plt.plot(x_potts, y_potts, ',', alpha=0.4, color='tab:blue')
plt.plot([min_val, max_val], [min_val, max_val], 'k--', linewidth=1)
plt.xlabel(r'$C^{ij}_{\alpha\beta}$, Natural MSA', fontsize=13)
plt.ylabel(r'$C^{ij}_{\alpha\beta}$, Generated MSA', fontsize=13)
plt.title('(a) Potts Model', fontsize=13, fontweight='bold')
plt.text(0.05, 0.95, f'r = {r_potts:.3f}',
         transform=plt.gca().transAxes, fontsize=12, ha='left', va='top')
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

# (b) MSA-T
plt.subplot(1, 3, 2)
plt.plot(x_msat, y_msat, ',', alpha=0.4, color='tab:orange')
plt.plot([min_val, max_val], [min_val, max_val], 'k--', linewidth=1)
plt.xlabel(r'$C^{ij}_{\alpha\beta}$, Natural MSA', fontsize=13)
plt.title('(b) MSA-T Model', fontsize=13, fontweight='bold')
plt.text(0.05, 0.95, f'r = {r_msat:.3f}',
         transform=plt.gca().transAxes, fontsize=12, ha='left', va='top')
plt.xticks(fontsize=13)
plt.yticks([], [])

# (c) Null Model
plt.subplot(1, 3, 3)
plt.plot(x_null, y_null, ',', alpha=0.4, color='tab:green')
plt.plot([min_val, max_val], [min_val, max_val], 'k--', linewidth=1)
plt.xlabel(r'$C^{ij}_{\alpha\beta}$, Natural MSA', fontsize=13)
plt.ylabel(r'$C^{ij}_{\alpha\beta}$, Reference MSA', fontsize=13)
plt.title('(c) Null Model', fontsize=13, fontweight='bold')
plt.text(0.05, 0.95, f'r = {r_null:.3f}',
         transform=plt.gca().transAxes, fontsize=12, ha='left', va='top')
plt.xticks(fontsize=13)
plt.yticks([], [])

plt.tight_layout(pad=1.2)
#plt.savefig("tbccr.eps", format='png', dpi=300)
plt.show()
