import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/Mohd Rizwan/Downloads/Da Project/Amazon Analysis Using Python/Python_Amazon_Sales_Analysis-main/Amazon Sale Report.csv")

df.shape
df.head()
df.describe()
df.info()

df.drop(["New", "PendingS"], axis= 1, inplace = True)

df.info()
pd.isnull(df).sum()

df.dropna(inplace= True)

pd.isnull(df).sum()

df.columns

df['ship-postal-code']=df['ship-postal-code'].astype(int)

df['ship-postal-code'].dtype

df['Date']=pd.to_datetime (df['Date'])

df.columns

df.rename(columns = {'Qty': 'Quantity'},inplace = True)

df.describe(include = 'object')

df[['Quantity', 'Amount']].describe()

ax = sns.countplot(x = 'Size', data = df, hue = 'Size')

ax = sns.countplot(x='Size' ,data=df, hue = 'Size')

for container in ax.containers:
    ax.bar_label(container)


s_qty = df.groupby(['Size'], as_index = False)['Quantity'].sum().sort_values(by = 'Quantity', ascending = False)

df.groupby(['Size'], as_index = False)['Quantity'].sum().sort_values(by = 'Quantity', ascending = False)
sns.barplot(x = 'Size', y ='Quantity', data = s_qty, hue = 'Size')


sns.countplot(data= df, x = 'Courier Status', hue = 'Status')
plt.show()


plt.figure(figsize = (10,5))
ax = sns.countplot(data = df, x = 'Courier Status', hue = 'Status')
plt.show()


df['Size'].hist()
plt.show()

df['Category'] = df['Category'].astype('str')
column_data = df['Category']
plt.figure(figsize= (10,5))
plt.hist(column_data, bins= 15, edgecolor = 'black')
plt.xticks(rotation = 90)
plt.show()


df.info()

B2b_check = df['B2B'].value_counts()
plt.pie(B2b_check, labels = B2b_check, autopct = '%1.2f%%')
plt.show()


B2b_Check = df['B2B'].value_counts()
plt.pie(B2b_Check, labels = B2b_Check.index, autopct = '%1.1f%%')
plt.show()


B2b_check = df['B2B'].value_counts()
plt.pie(B2b_check, labels = B2b_check, autopct = '%1.2f%%')
plt.show()


a1 = df['Fulfilment'].value_counts()
fig, ax = plt.subplots()
ax.pie(a1, labels = a1.index, autopct= '%1.1f%%', radius = 0.7, wedgeprops = dict(width = 0.6))
ax.set(aspect='equal')
plt.show()


a1 = df['Fulfilment'].value_counts()
fig, ax = plt.subplots()
ax.pie(a1, labels = a1.index, autopct= '%1.1f%%', radius = 0.7, wedgeprops = dict(width = 0.6))
ax.set(aspect='equal')
plt.show()



x_data = df['Category']
y_data = df['Size']
plt.scatter(x_data, y_data)
plt.xlabel('Category')
plt.ylabel('Size')
plt.title('Scatter Plot')
plt.show()


top_10 = df['ship-state'].value_counts().head(10)
plt.figure(figsize = (12, 6))
sns.countplot(data = df[df['ship-state'].isin(top_10.index)], x = 'ship-state', hue = 'ship-state')
plt.xlabel('Ship State')
plt.ylabel('Count')
plt.title('Distribution of State')
plt.xticks(rotation = 90)
plt.show()

## Conclusion
### This concludes the project, this project is my first python project done for the prupose of learning more about data analytics and to gain more insights and fine tuned results.
##### PS: It might seem that everything has been forced into this single project, however in my defence this is my first project and am more focused on the learning and exploring part, will definitely get better at my craft as I go on.
#### You can find the guided project on Youtube (https://youtu.be/1TmrFEHTg54?si=m7kSeGbEKot_rLVx) and you can find me on LinkedIn (https://www.linkedin.com/in/mohd-rizwan-971399244?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)