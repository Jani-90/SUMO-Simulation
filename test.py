import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Pie chart (without autopct)
fig, ax = plt.subplots()
wedges, texts = ax.pie(sizes, labels=labels, startangle=90)

# Calculate percentages
percentages = [f'{size / sum(sizes) * 100:.1f}%' for size in sizes]

# Customize the legend
ax.legend(wedges, [f'{label}: {pct}' for label, pct in zip(labels, percentages)], title="Categories")

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

plt.show()