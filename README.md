# Amazon-analysis
```python
"""
Introduction:

This Python project explores Amazon sales data, aiming to sharpen data analysis skills and uncover interesting patterns. 
Using libraries like NumPy, Pandas, Matplotlib, and Seaborn, the focus is on understanding product sizes, the impact of 
order fulfillment, and key sales metrics. Through data cleaning and visualization, the project aims to reveal trends 
and insights, enhancing our understanding of Amazon sales dynamics.

"""


# We start by importing essential libraries for our data analysis and visualization tasks.
import numpy as np  # NumPy is used for numerical operations.
import pandas as pd  # Pandas is employed for data manipulation and analysis.
import matplotlib.pyplot as plt  # Matplotlib is essential for basic plotting.
import seaborn as sns  # Seaborn is a powerful library for statistical data visualization.

# Now, we load our dataset from a CSV file into a Pandas DataFrame named 'df'.
df = pd.read_csv("C:/Users/Mohd Rizwan/Downloads/Da Project/Amazon Analysis Using Python/Python_Amazon_Sales_Analysis-main/Amazon Sale Report.csv")

# To understand the structure of our dataset, we explore its dimensions, initial rows, and statistical summary.
# This helps us get a quick overview of the data we are working with.
df.shape  # Provides the number of rows and columns in the dataset
df.head()  # Displays the first few rows of the dataset
df.describe()  # Generates descriptive statistics for numerical columns
df.info()  # Presents a concise summary of the dataset, including data types and missing values.

# As part of data cleaning, we remove unnecessary columns ('New' and 'PendingS') and any rows with missing values.
df.drop(["New", "PendingS"], axis=1, inplace=True)
df.dropna(inplace=True)

# Next, we perform data type conversions for better analysis.
# We convert the 'ship-postal-code' column to integer and the 'Date' column to datetime.
df['ship-postal-code'] = df['ship-postal-code'].astype(int)
df['Date'] = pd.to_datetime(df['Date'])

# Additionally, we rename the 'Qty' column to 'Quantity' for clarity in our analysis.
df.rename(columns={'Qty': 'Quantity'}, inplace=True)

# To understand the categorical variables better, we generate descriptive statistics specifically for them.
df.describe(include='object')

# Moving on to visualizations, we create a count plot for the 'Size' column, adding labels to represent the counts on the bars.
ax = sns.countplot(x='Size', data=df, hue='Size')
for container in ax.containers:
    ax.bar_label(container)

# We continue with a grouped bar plot to showcase the relationship between 'Size' and 'Quantity'.
# This involves grouping by 'Size', summing the 'Quantity', and creating a bar plot.
s_qty = df.groupby(['Size'], as_index=False)['Quantity'].sum().sort_values(by='Quantity', ascending=False)
sns.barplot(x='Size', y='Quantity', data=s_qty, hue='Size')

# Visualizing the distribution of 'Courier Status' with 'Status' as hue using count plots.
sns.countplot(data=df, x='Courier Status', hue='Status')
plt.show()

# A larger count plot for 'Courier Status' with 'Status' as hue, setting a specific figure size.
plt.figure(figsize=(10, 5))
ax = sns.countplot(data=df, x='Courier Status', hue='Status')
plt.show()

# A histogram representing the distribution of 'Size'.
df['Size'].hist()
plt.show()

# A histogram for the 'Category' column after converting it to string, with specified bins and rotation.
df['Category'] = df['Category'].astype('str')
column_data = df['Category']
plt.figure(figsize=(10, 5))
plt.hist(column_data, bins=15, edgecolor='black')
plt.xticks(rotation=90)
plt.show()

# We move on to pie charts, starting with one for the value counts of 'B2B'.
B2b_check = df['B2B'].value_counts()
plt.pie(B2b_check, labels=B2b_check.index, autopct='%1.2f%%')
plt.show()

# Another pie chart for 'B2B' value counts, but with a different percentage format.
B2b_check = df['B2B'].value_counts()
plt.pie(B2b_check, labels=B2b_check.index, autopct='%1.1f%%')
plt.show()

# A pie chart for 'Fulfilment' value counts, utilizing specific settings for appearance.
a1 = df['Fulfilment'].value_counts()
fig, ax = plt.subplots()
ax.pie(a1, labels=a1.index, autopct='%1.1f%%', radius=0.7, wedgeprops=dict(width=0.6))
ax.set(aspect='equal')
plt.show()

# A scatter plot to visualize the relationship between 'Category' and 'Size'.
x_data = df['Category']
y_data = df['Size']
plt.scatter(x_data, y_data)
plt.xlabel('Category')
plt.ylabel('Size')
plt.title('Scatter Plot')
plt.show()

# Finally, a count plot for the top 10 'ship-state' values with specified settings.
top_10 = df['ship-state'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.countplot(data=df[df['ship-state'].isin(top_10.index)], x='ship-state', hue='ship-state')
plt.xlabel('Ship State')
plt.ylabel('Count')
plt.title('Distribution of State')
plt.xticks(rotation=90)
plt.show()


"""
Conclusion:

To sum it up, this project provided hands-on experience in analyzing Amazon sales data. By exploring 
product sizes, order fulfillment, and sales metrics, I gained practical insights. Cleaning the data and creating visuals 
contributed to a deeper understanding of Amazon sales dynamics. It's been a journey of learning through real-world data analysis.
"""
```
![screencapture-github-Rizwans-github-Amazon-analysis-blob-main-Analysis-on-python-py-2024-01-10-04_24_26](https://github.com/Rizwans-github/Amazon-analysis/assets/141806496/a142b640-9f03-493a-8895-c56c463c164d)

![screencapture-localhost-8888-notebooks-Downloads-Da-Project-Amazon-Analysis-Using-Python-Amazon-Sales-DA-project-ipynb-2024-01-08-16_19_23](https://github.com/Rizwans-github/Amazon-analysis/assets/141806496/b59441b5-df94-4349-9604-e07a1d209b96)
