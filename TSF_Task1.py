#!/usr/bin/env python
# coding: utf-8

# # The Sparks Foundation #GRIPFEB2021
# # Name- Sahil Sejwal
# # Task -Perform exploratory Data Analysis on a Terrorism Dataset
# # As a security/defence analyst we had to find out hot zone of terrorism

# # Importing the Libraries

# In[6]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # Provision to ignore the warnings

# In[7]:


import warnings
warnings.filterwarnings("ignore")


# # Reading and Displaying the dataset

# In[10]:


df=pd.read_csv("Terrorism.csv", encoding = 'latin1')


# In[11]:


df


# # Renaming the columns

# In[12]:


df.rename(columns={'iyear':'Year','imonth':'Month','iday':"day",'gname':'Group','country_txt':'Country','region_txt':'Region','provstate':'State','city':'City',
    'attacktype1_txt':'Attacktype','targtype1_txt':'Targettype','weaptype1_txt':'Weapon','nkill':'kill',
     'nwound':'Wound', 'natlty1_txt':'nationality'},inplace=True)
df


# # Rearranging the columns

# In[13]:


data=df[['Year','Month','day','Group','Country','Region','State','City','latitude','longitude','summary','location','Attacktype','Targettype','Weapon','kill','Wound','nationality','motive','target1']]
data


# # Having a look dataset

# In[14]:


data.shape


# In[15]:


data.describe(include = 'all')


# # Handling null values

# In[16]:


data.isnull().sum()


# In[17]:


data['Wound']=data['Wound'].fillna(0)
data['kill']=data['kill'].fillna(0)


# In[18]:


data['total damage to lives']=data['Wound']+data['kill']
data[['Wound','kill','total damage to lives']].head()


# # Analysis

# In[19]:


numberofyears =data['Year'].unique()
plt.rcParams.update({'font.size': 50})
plt.rcParams['figure.figsize']=75,30
numberofkills =data['Year'].value_counts()
sns.lineplot(x= numberofyears, y= numberofkills)
plt.title('History of attacks over the years',fontsize=70)
plt.xlabel('Years',fontsize=70)
plt.ylabel('Number of Attacks',fontsize=100)
plt.show()


# # Most affected region

# In[20]:


temp=data.groupby(['Region'])['total damage to lives'].sum().sort_values(ascending=False)
plt.rcParams['figure.figsize']=75,30
sns.barplot(x=temp.index,y=temp.values.reshape(-1))
plt.title("Affected region",fontsize=70)
plt.xlabel('Region',fontsize=70)
plt.ylabel('Number of People Died',fontsize=70)
plt.xticks(rotation=90)
plt.show()


# # Most attacked country

# In[21]:


attack=data.Country.value_counts()[:10]
plt.rcParams['figure.figsize']=75,30
sns.barplot(x=attack.index,y=attack.values)
plt.title('Most Attacked Country',fontsize=40)
plt.xlabel('Country',fontsize=40)
plt.ylabel('Number of Attacks',fontsize=40)
plt.xticks(rotation=90)
plt.show()


# # Target Type

# In[22]:


plt.rcParams.update({'font.size': 20})
hel = data['Targettype'].value_counts().drop('Unknown')[:10]  
plt.figure(figsize = (22,8))
plt.pie(hel.values, labels=hel.index)
plt.show()


# # Country wise number of attacks

# In[23]:


plt.rcParams.update({'font.size': 50}) 
plt.rcParams['figure.figsize']=75,30
ty = data['Group'].value_counts()[:20]
plt.figure(figsize = (50,10))
sns.barplot(x=ty.index, y=ty.values,color ='red')
plt.xlabel('City name',fontsize = 40)
plt.ylabel('Kills',fontsize = 40)
plt.title('Groups involved in attack',fontsize = 40)
plt.xticks(rotation = 90)
plt.show()


# # Type of attack

# In[24]:


plt.rcParams.update({'font.size': 50}) 
plt.rcParams['figure.figsize']=75,30
sns.countplot(y=data['Attacktype'], palette='inferno')
plt.xlabel('Attack type',fontsize = 70)
plt.ylabel('No of attacks',fontsize = 70)
plt.rcParams.update({'font.size': 30})
plt.title('Attack Type',fontsize = 60)
plt.show()


# # Most Affected City

# In[25]:


plt.rcParams.update({'font.size':15})
ty = data['City'].value_counts().drop('Unknown')[:15]
plt.figure(figsize = (22,8))
plt.pie(ty.values, labels=ty.index)
plt.show()


# # Conlusion
# 1. Number of kills have been decreasing in each decade since 1970
# 2. The hottest zone for terror attacks is Middle East and North Africa followed by South Asia
# 3. The maximum number of attacks took place in Iraq
# 4. Bagdhad is the city which is most affected
# 5. Bombing/Explosion is the most common type of attack
# 6. Most number of attacks were done by unknown terrorist groups and second highest were by Taliban
# 7. The most common targets were citizens as compared to Military people, police people etc
