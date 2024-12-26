import pandas as pd

# Sample data (replace with your actual data source)
data = {'date': ['1/1/2024', '1/2/2024', '1/3/2024', '1/4/2024', '1/5/2024', '1/6/2024', '1/7/2024'],
        'sales': [100, 150, 200, 250, 300, 120, 80]}
df = pd.DataFrame(data)

# Extract the week number from the date
df['week'] = df['date'].dt.isocalendar().week

# Calculate weekly sales by grouping by week number and summing sales
weekly_sales = df.groupby('week')['sales'].sum()

# Print the weekly sales
print(weekly_sales)