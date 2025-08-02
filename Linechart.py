
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Load CSV
df = pd.read_csv('/home/kcee/Documents/Bpostdrive/downloads/house_sales_cleaned.csv')

df['sale_date'] = pd.to_datetime(df['sale_date'])

# Group by month and average price
monthly_avg = df.groupby(df['sale_date'].dt.to_period('M'))['sale_price'].mean()

monthly_avg.plot(kind='line', marker='o')
plt.title('Average Sale Price Over Time')
plt.xlabel('Month')
plt.ylabel('Average Sale Price')
plt.xticks(rotation=45)
plt.show()
# Insight: How are prices trending over months or years?