# Real_Estate_Analysis

# 🏠 House Sales Data Analysis & Visualization

This project provides a comprehensive analysis and visualization of house sales data using **Python**, **Pandas**, **Matplotlib**, and **Seaborn**. The visualizations explore trends, correlations, and distributions in the dataset to extract meaningful insights about housing prices, sizes, locations, and more.

---

## 📊 Visualizations Included

### 1. **Bar Chart — Average Sale Price by City**
- Compares average home prices across different cities.
- **Insight**: Helps identify cities with the highest and lowest housing costs.

### 2. **Correlation Heatmap**
- Displays correlation between numerical features such as:
  - Sale price
  - Number of bedrooms
  - Months listed
  - Area in square meters
- **Insight**: Shows which factors are most closely related to pricing.

### 3. **Line Chart — Average Sale Price Over Time**
- Shows price trends over months/years.
- **Insight**: Detect market trends and seasonal patterns in pricing.

### 4. **Pie Chart — House Type Distribution**
- Displays proportion of house types (Detached, Semi-detached, etc.)
- Includes legend with color-coded key.
- **Insight**: Understand which house types are most common.

### 5. **Scatter Plot — Area vs Sale Price**
- Plots sale price against property area.
- Color-coded by bedroom count.
- **Insight**: Are larger houses more expensive? Does bedroom count influence price?

---

## 📦 Requirements

To run the scripts, you’ll need the following Python libraries installed:

```bash
pip install pandas matplotlib seaborn

## DataSet Used

# Load CSV
df = pd.read_csv('/home/kcee/Documents/Bpostdrive/downloads/house_sales_cleaned.csv')

Any User can added their choice of dataset to work with