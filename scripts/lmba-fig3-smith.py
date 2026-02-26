"""Fig.3: Smith chart showing impedance modulation by CSP injection."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

fig, ax = plt.subplots(1, 1, figsize=(7, 7))
ax.set_aspect('equal')
ax.set_xlim(-1.15, 1.15)
ax.set_ylim(-1.15, 1.15)
ax.set_title('CSP Injection: Impedance Modulation on Smith Chart', fontsize=13, pad=15)

# Draw Smith chart background
# Unit circle
unit_circle = Circle((0, 0), 1, fill=False, color='gray', linewidth=0.8)
ax.add_patch(unit_circle)

# Constant resistance circles (r = 0, 0.5, 1, 2, 5)
for r in [0, 0.5, 1, 2, 5]:
    center = (r / (1 + r), 0)
    radius = 1 / (1 + r)
    c = Circle(center, radius, fill=False, color='lightgray', linewidth=0.5, linestyle='-')
    ax.add_patch(c)

# Constant reactance arcs (x = ±0.5, ±1, ±2)
theta = np.linspace(0, np.pi, 200)
for x in [0.5, 1, 2]:
    cx, cy = 1, 1/x
    r_arc = 1/abs(x)
    arc_x = cx + r_arc * np.cos(theta)
    arc_y_pos = cy + r_arc * np.sin(theta)
    arc_y_neg = -cy - r_arc * np.sin(theta)
    # Clip to unit circle
    for arc_y in [arc_y_pos, arc_y_neg]:
        mask = arc_x**2 + arc_y**2 <= 1.01
        ax.plot(arc_x[mask], arc_y[mask], color='lightgray', linewidth=0.4)

# Horizontal axis
ax.axhline(0, color='lightgray', linewidth=0.5)

# Z0 point (center)
ax.plot(0, 0, 'ko', markersize=6)
ax.annotate('Z₀ = 50 Ω', xy=(0, 0), xytext=(0.08, -0.12), fontsize=9)

# Alpha contours (constant CSP power ratio)
# |rho|^2 = alpha / (alpha + 2)
# These are circles centered at origin on Smith chart
alphas = [0.1, 0.25, 0.5, 1.0]
colors_alpha = ['#2ecc71', '#3498db', '#e67e22', '#e74c3c']
labels_alpha = ['α=0.1 (-13 dB)', 'α=0.25 (-9 dB)', 'α=0.5 (-6 dB)', 'α=1.0 (-3 dB)']

for alpha, color, label in zip(alphas, colors_alpha, labels_alpha):
    rho_mag = np.sqrt(alpha / (alpha + 2))
    circle = Circle((0, 0), rho_mag, fill=False, color=color, linewidth=2, linestyle='-', label=label)
    ax.add_patch(circle)
    # Label the impedance at real axis
    z_real = 50 * (1 + rho_mag) / (1 - rho_mag)
    z_real_low = 50 * (1 - rho_mag) / (1 + rho_mag)

# Phase rotation arrows for alpha=0.5
rho_05 = np.sqrt(0.5 / 2.5)
theta_arrow = np.linspace(0, 2*np.pi, 100)
ax.plot(rho_05 * np.cos(theta_arrow), rho_05 * np.sin(theta_arrow),
        color='#e67e22', linewidth=2, alpha=0.3)

# Example impedance points for alpha=0.5
angles_deg = [0, 90, 180, 270]
for ang in angles_deg:
    ang_rad = np.radians(ang)
    px = rho_05 * np.cos(ang_rad)
    py = rho_05 * np.sin(ang_rad)
    ax.plot(px, py, 'o', color='#e67e22', markersize=8)

# Arrow showing phase rotation
arrow = FancyArrowPatch(
    (rho_05, 0.03), (0.03, rho_05),
    arrowstyle='->', mutation_scale=15,
    color='#e67e22', linewidth=1.5
)
ax.add_patch(arrow)
ax.annotate('CSP phase\nrotation', xy=(rho_05*0.7, rho_05*0.7),
            fontsize=9, color='#e67e22', ha='center')

# Real-axis impedance annotations
ax.annotate('25 Ω', xy=(rho_05 * np.cos(np.pi), 0), xytext=(-0.65, 0.1),
            fontsize=9, color='#e67e22')
ax.annotate('100 Ω', xy=(rho_05, 0), xytext=(rho_05 + 0.05, 0.08),
            fontsize=9, color='#e67e22')

# Legend
ax.legend(loc='lower left', fontsize=9, framealpha=0.9,
          title='CSP power ratio (α = P_CSP/P_BPA)', title_fontsize=9)

ax.set_xlabel('Real(Γ)', fontsize=10)
ax.set_ylabel('Imag(Γ)', fontsize=10)

plt.figtext(0.5, 0.01, 'Based on analysis from [1][2]', ha='center', fontsize=8, color='gray')
plt.tight_layout()
plt.savefig('/home/raspi5/zenn-articles/images/lmba-fundamentals/lmba-fundamentals-03-smith-chart.png',
            dpi=150, bbox_inches='tight', facecolor='white')
print("Fig.3 saved successfully.")
