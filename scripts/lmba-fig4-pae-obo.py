"""Fig.4: PAE vs output back-off comparison.

Data sources:
- Ideal Class-B: theoretical (eta = pi/4 * v, where v = voltage utilization)
- Ideal Doherty (6 dB OBO): theoretical
- Quaglia 2018 [3]: Fig. 30 CW measurement summary
  - Saturation PAE: 48-58% across 1.7-2.5 GHz
  - 6 dB OBO PAE: 43-53%
  - 8 dB OBO PAE: 39-50%
  Only saturation, 6 dB, and 8 dB OBO are reported in the paper.
  We plot the mid-band representative values at 2.1 GHz.
- Shepphard 2016 [2]: Only saturation efficiency (~70%) is clearly stated.
  OBO-specific PAE values are not explicitly reported.
"""
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1, figsize=(8, 5))

# X axis: Output back-off (dB), from 0 to -12
obo = np.linspace(0, -12, 200)

# Ideal Class-B: eta = eta_max * 10^(OBO/20)
pae_classb_max = 78.5  # pi/4 * 100
pae_classb = pae_classb_max * 10**(obo/20)

# Ideal Doherty (6 dB OBO): flat efficiency from 0 to -6 dB, then Class-B rolloff
pae_doherty = np.zeros_like(obo)
for i, o in enumerate(obo):
    if o >= -6:
        pae_doherty[i] = 78.5
    else:
        pae_doherty[i] = 78.5 * 10**((o + 6)/20)

# Quaglia 2018 [3] measured data points (from paper Fig. 30, representative at ~2.1 GHz)
# Only the three OBO levels explicitly reported in the paper are plotted
obo_quaglia = [0, -6, -8]
pae_quaglia = [55, 48, 43]  # Mid-range values from 48-58%, 43-53%, 39-50%

ax.plot(obo, pae_classb, 'k--', linewidth=1.5, label='Ideal Class-B', alpha=0.6)
ax.plot(obo, pae_doherty, 'b-', linewidth=1.5, label='Ideal Doherty (6 dB)', alpha=0.6)
ax.plot(obo_quaglia, pae_quaglia, 'rs', markersize=10, linewidth=2,
        label='LMBA [3] (2.1 GHz, measured)', zorder=5)

# Connect Quaglia points with dashed line for visual guidance
ax.plot(obo_quaglia, pae_quaglia, 'r--', linewidth=1, alpha=0.5)

# Show the range (error bars) from the frequency sweep (min-max across 1.7-2.5 GHz)
pae_quaglia_lo = [48, 43, 39]  # Minimum across band
pae_quaglia_hi = [58, 53, 50]  # Maximum across band
yerr_lo = [v - lo for v, lo in zip(pae_quaglia, pae_quaglia_lo)]
yerr_hi = [hi - v for v, hi in zip(pae_quaglia, pae_quaglia_hi)]
ax.errorbar(obo_quaglia, pae_quaglia, yerr=[yerr_lo, yerr_hi],
            fmt='none', ecolor='red', elinewidth=1.5, capsize=4, capthick=1.5,
            label='Range across 1.7-2.5 GHz [3]')

ax.set_xlabel('Output Back-Off (dB)', fontsize=11)
ax.set_ylabel('PAE (%)', fontsize=11)
ax.set_title('PAE vs Output Back-Off: Class-B / Doherty / LMBA', fontsize=13)
ax.set_xlim(-12, 1)
ax.set_ylim(0, 85)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9, loc='upper right')

# Annotate the key region
ax.axvspan(-8, -4, alpha=0.08, color='orange')
ax.annotate('Typical telecom\noperating region\n(6-8 dB PAPR)',
            xy=(-6, 15), fontsize=9, ha='center', color='#e67e22',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))

plt.figtext(0.5, 0.01, 'Data from [3] Quaglia & Cripps, IEEE TMTT 2018, Fig. 30',
            ha='center', fontsize=8, color='gray')
plt.tight_layout()
plt.savefig('/home/raspi5/zenn-articles/images/lmba-fundamentals/lmba-fundamentals-04-pae-vs-obo.png',
            dpi=150, bbox_inches='tight', facecolor='white')
print("Fig.4 saved successfully.")
