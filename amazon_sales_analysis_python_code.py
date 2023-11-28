#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[8]:


import seaborn as sns


# In[9]:


# loading the data set


# In[ ]:


C:\Users\Dell\OneDrive\Desktop\New folder\Python_Amazon_Sales_Analysis-main


# In[5]:


df = pd.read_csv(r'C:\Users\Dell\OneDrive\Desktop\New folder\Python_Amazon_Sales_Analysis-main\Amazon Sale Report.csv' ,encoding = 'unicode_escape')


# In[14]:





# In[ ]:


# exploratory data analysis and data cleaning


# In[6]:


df.head()


# In[7]:


df.tail()


# In[8]:


df.info()


# In[9]:


df.shape


# In[11]:


# drop unrelated/blank column
df.drop(['New','PendingS'], axis = 1, inplace = True)


# In[12]:


df.info()


# In[13]:


pd.isnull(df)


# In[14]:


pd.isnull(df).sum()


# In[ ]:


# drop null values


# In[15]:


df.dropna(inplace= True)


# In[16]:


df.shape


# In[17]:


df.columns


# In[ ]:


#change data type


# In[19]:


df['ship-postal-code']=df['ship-postal-code'].astype('int')


# In[20]:


df['ship-postal-code'].dtype


# In[22]:


df['Date']=pd.to_datetime (df['Date'])


# In[24]:


df.columns


# In[25]:


# Rename columns
df.rename(columns={'Qty':'Quantity'})


# In[26]:


# Describe( )method return discription of the data in the Dataframe (i.e. count, mean,std,min.etc)
df.describe()


# In[27]:


df.describe(include='object')


# In[28]:


#use describe() for specific columns
df[['Qty','Amount']].describe()


# In[ ]:


# Exploratory data analysis


# In[29]:


df.columns


# In[ ]:


#size


# In[34]:


ax=sns.countplot(x='Size' , data= df)


# In[36]:


ax=sns.countplot(x='Size' , data= df)
   
for bars in ax.containers:
       ax.bar_label(bars)


# In[ ]:


# Group by


# In[40]:


df.groupby(['Size'], as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)


# In[44]:


S_Qty=df.groupby(['Size'],as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)

sns.barplot(x='Size',y= 'Qty',data=S_Qty)


# In[ ]:


# Courier Status


# In[ ]:


sns.countplot(data=df, x='Courier Status', hue = 'Status')


# In[45]:


plt.figure(figsize=(10,5))

ax=sns.countplot(data=df,x='Courier Status' ,hue='Status')

plt.show()


# In[49]:


# Histogram
df['Size'].hist()


# In[55]:


df['Category'] =df['Category'].astype(str)
column_data =df['Category']
plt.figure(figsize =(10,5))
plt.hist(column_data,bins= 30 ,edgecolor = 'white')
plt.xticks(rotation=90)
plt.show()


# In[50]:


df.info()


# In[57]:


# checking B2B Data by using pie chart
B2B_Check = df['B2B'].value_counts()

# plot the pie count
plt.pie(B2B_Check, labels=B2B_Check, autopct='%1.1f%%')

# plt.axis('equal')
plt.show()


# In[58]:


# checking B2B Data by using pie chart
B2B_Check = df['B2B'].value_counts()


# plot the pie chart
plt.pie(B2B_Check,labels=B2B_Check.index, autopct= '%1.1f%%')

# plt.axis('equal')
plt.show()


# In[60]:


# prepare data for scatter plot
x_data = df['Category']
y_data = df['Size']

#Plot the Scatter plot
plt.scatter(x_data, y_data)
plt.xlabel('Category')
plt.ylabel('Size')
plt.title('Scatter Plot')
plt.show()


# In[62]:


# plot count of cities by states
plt.figure(figsize=(12,5))
sns.countplot(data=df, x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=90)
plt.show()


# In[64]:


# top _10_states
top_10_state = df['ship-state'].value_counts().head(10)

# plot count of cities by state 
plt.figure(figsize=(12,6))
sns.countplot(data=df[df['ship-state'].isin(top_10_state.index)], x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=90)
plt.show()


# In[ ]:




