import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load CSV
df = pd.read_csv('/home/kcee/Documents/Bpostdrive/downloads/house_sales_cleaned.csv')

# Prepare data
house_counts = df['house_type'].value_counts()
labels = house_counts.index
sizes = house_counts.values
colors = sns.color_palette('pastel')[0:len(labels)]  # Custom palette

# Create pie chart
fig, ax = plt.subplots(figsize=(8, 6))  # Larger figure for clarity

# Pie chart with better visual options
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=None,  # We'll use a legend instead
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    textprops={'fontsize': 12, 'color': 'black'},
    wedgeprops={'edgecolor': 'white'}
)

# Improve percentage text style
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

# Add legend (the key)
ax.legend(
    wedges,
    labels,
    title="House Type",
    title_fontsize=13,
    fontsize=11,
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Title and layout
plt.title('House Type Distribution', fontsize=16, fontweight='bold')
plt.ylabel('')  # Hide y-axis label
plt.tight_layout()
plt.show()
