
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Load CSV
df = pd.read_csv('/home/kcee/Documents/Bpostdrive/downloads/house_sales_cleaned.csv')

# Clean 'area' column first
df['area_sqm'] = df['area'].str.replace(' sq.m.', '').astype(float)

sns.scatterplot(data=df, x='area_sqm', y='sale_price', hue='bedrooms', palette='viridis')
plt.title('Area vs Sale Price (Colored by Bedrooms)')
plt.xlabel('Area (sq.m.)')
plt.ylabel('Sale Price')
plt.show()

#Insight: Are bigger houses more expensive? Does bedroom count play a role?

