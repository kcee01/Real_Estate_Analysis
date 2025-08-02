import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Load CSV
df = pd.read_csv('/home/kcee/Documents/Bpostdrive/downloads/house_sales_cleaned.csv')

#Bar Chart — Compare Categories
sns.barplot(data=df, x='city', y='sale_price', estimator='mean', ci=None)
plt.title('Average Sale Price by City')
plt.xlabel('City')
plt.ylabel('Average Sale Price')
plt.xticks(rotation=45)
plt.show()

#Insight: Which cities have the highest or lowest average home prices?
