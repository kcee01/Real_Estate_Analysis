import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv('/home/kcee/Documents/Bpostdrive/downloads/house_sales_cleaned.csv')

# Clean 'area' column: remove " sq.m." and convert to float
df['area_sqm'] = df['area'].str.replace(' sq.m.', '').astype(float)

# Select numerical columns only
numeric = df[['sale_price', 'bedrooms', 'months_listed', 'area_sqm']]
corr = numeric.corr()

# Plot correlation heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
#Visualize correlation between numerical features: