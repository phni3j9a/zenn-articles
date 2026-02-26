"""Fig.2: LMBA basic circuit diagram using matplotlib (block diagram style)."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(-1, 13)
ax.set_ylim(-3, 7)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Load-Modulated Balanced Amplifier (LMBA)', fontsize=14, pad=15)

def draw_box(ax, x, y, w, h, text, color='white', edgecolor='black', fontsize=10):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                         facecolor=color, edgecolor=edgecolor, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=fontsize)

def draw_arrow(ax, x1, y1, x2, y2, color='black'):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

def draw_line(ax, x1, y1, x2, y2, color='black', ls='-'):
    ax.plot([x1, x2], [y1, y2], color=color, linewidth=1.5, linestyle=ls)

# Input coupler
draw_box(ax, 1.5, 2.5, 2, 2.5, '90° Hybrid\nCoupler\n(Input)', color='#f0f0f0')

# BPA1 (upper)
draw_box(ax, 5, 4.2, 2, 1.2, 'BPA₁', color='#e8f5e9', edgecolor='#4caf50')

# BPA2 (lower)
draw_box(ax, 5, 2.1, 2, 1.2, 'BPA₂', color='#e8f5e9', edgecolor='#4caf50')

# Output coupler
draw_box(ax, 8.5, 2.5, 2, 2.5, '90° Hybrid\nCoupler\n(Output)', color='#f0f0f0')

# CSP PA
draw_box(ax, 8.5, -0.5, 2, 1.2, 'CSP PA', color='#e3f2fd', edgecolor='#1976d2')

# RF Input
ax.text(0.2, 3.75, 'RF\nInput', ha='center', va='center', fontsize=11, fontweight='bold')
draw_arrow(ax, 0.7, 3.75, 1.5, 3.75)

# Input coupler -> BPA1 (0° path)
draw_arrow(ax, 3.5, 4.2, 5, 4.8)
ax.text(4.2, 4.85, '0°', fontsize=9, color='gray')

# Input coupler -> BPA2 (-90° path)
draw_arrow(ax, 3.5, 3.2, 5, 2.7)
ax.text(4.2, 2.65, '-90°', fontsize=9, color='gray')

# BPA1 -> Output coupler
draw_arrow(ax, 7, 4.8, 8.5, 4.2)

# BPA2 -> Output coupler
draw_arrow(ax, 7, 2.7, 8.5, 3.2)

# Output -> RF Output
draw_arrow(ax, 10.5, 3.75, 11.8, 3.75)
ax.text(12.2, 3.75, 'RF\nOutput', ha='center', va='center', fontsize=11, fontweight='bold')
ax.text(11.2, 4.1, 'Σ port', fontsize=9, color='gray')

# Output coupler isolated port -> CSP
draw_line(ax, 9.5, 2.5, 9.5, 0.7)
ax.annotate('', xy=(9.5, 0.7), xytext=(9.5, 2.5),
            arrowprops=dict(arrowstyle='<->', color='#1976d2', lw=1.5))
ax.text(10.1, 1.6, 'Isolated\nport', fontsize=9, color='gray', ha='left')

# CSP input
draw_arrow(ax, 9.5, -2.0, 9.5, -0.5, color='#1976d2')
ax.text(9.5, -2.5, 'Control Signal\n(Amplitude & Phase)', ha='center', va='center',
        fontsize=10, color='#1976d2', fontweight='bold')

# Annotation box
ax.text(5.5, 6.2,
        'CSP injection at isolated port modulates\n'
        'the load impedance seen by BPA₁ and BPA₂',
        ha='center', va='center', fontsize=9, color='#1976d2',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#e3f2fd', edgecolor='#1976d2', alpha=0.8))

# Impedance labels
ax.text(4.3, 4.2, 'Z₁', fontsize=10, color='#4caf50')
ax.text(4.3, 3.1, 'Z₂', fontsize=10, color='#4caf50')

plt.tight_layout()
plt.savefig('/home/raspi5/zenn-articles/images/lmba-fundamentals/lmba-fundamentals-02-circuit-diagram.png',
            dpi=150, bbox_inches='tight', facecolor='white')
print("Fig.2 saved successfully.")
