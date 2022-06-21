
# coding: utf-8

# ## Build a simple trading strategy 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# ### 1. Munging the stock data and add two columns - MA10 and MA50

# In[4]:


#import FB's stock data, add two columns - MA10 and MA50
#use dropna to remove any "Not a Number" data
fb = pd.DataFrame.from_csv('../data/facebook.csv')
fb['MA10'] = fb['Close'].rolling(10).mean()
fb['MA50'] = fb['Close'].rolling(50).mean()
fb = fb.dropna()
fb.head()


# ### 2. Add "Shares" column to make decisions base on the strategy 

# In[6]:


#Add a new column "Shares", if MA10>MA50, denote as 1 (long one share of stock), otherwise, denote as 0 (do nothing)

fb['Shares'] = [1 if fb.loc[ei, 'MA10']>fb.loc[ei, 'MA50'] else 0 for ei in fb.index]


# In[7]:


#Add a new column "Profit" using List Comprehension, for any rows in fb, if Shares=1, the profit is calculated as the close price of 
#tomorrow - the close price of today. Otherwise the profit is 0.

#Plot a graph to show the Profit/Loss

fb['Close1'] = fb['Close'].shift(-1)
fb['Profit'] = [fb.loc[ei, 'Close1'] - fb.loc[ei, 'Close'] if fb.loc[ei, 'Shares']==1 else 0 for ei in fb.index]
fb['Profit'].plot()
plt.axhline(y=0, color='red')


# ### 3. Use .cumsum() to display our model's performance if we follow the strategy 

# In[8]:


#Use .cumsum() to calculate the accumulated wealth over the period

fb['wealth'] = fb['Profit'].cumsum()
fb.tail()


# In[12]:


#plot the wealth to show the growth of profit over the period

fb['wealth'].plot()
plt.title('Total money you win is {}'.format(fb.loc[fb.index[-2], 'wealth']))


# ## You can create your own simple trading strategy by copying the codes above and modify the codes accordingly using the data of Microsoft (microsoft.csv).

# ### So, let's get to work. (づ｡◕‿‿◕｡)づ

# In[4]:


# 1. Munging the stock data and add two columns - MA10 and MA50
ms_data = pd.DataFrame.from_csv("../data/microsoft.csv")
ms_data["MA10"] = ms_data["Close"].rolling(10).mean()
ms_data["MA50"] = ms_data["Close"].rolling(50).mean()
ms_data = ms_data.dropna()
ms_data.head()


# In[5]:


# 2. Add "Shares" column to make decisions base on the strategy

#Add a new column "Shares", if MA10>MA50, denote as 1 (long one share of stock), otherwise, denote as 0 (do nothing)
ms_data["Shares"] = [1 if ms_data.loc[ei, "MA10"] > ms_data.loc[ei, "MA50"] else 0 for ei in ms_data.index]


# In[8]:


#Add a new column "Profit" using List Comprehension, for any rows in fb, if Shares=1, the profit is calculated as the close price of 
#tomorrow - the close price of today. Otherwise the profit is 0.

ms_data["Close_1"] = ms_data["Close"].shift(-1)

ms_data["Profit"] = [
    ms_data.loc[
        ei, 
        "Close_1"
    ] - ms_data.loc[
        ei, 
        "Close"
    ] if ms_data.loc[
        ei, 
        "Shares"
    ] == 1 
    else 0 
    for ei in ms_data.index
]

#Plot a graph to show the Profit/Loss
ms_data["Profit"].plot()
plt.axhline(y=0, color="red")


# In[9]:


# 3. Use .cumsum() to display our model's performance if we follow the strategy

#Use .cumsum() to calculate the accumulated wealth over the period

ms_data["wealth"] = ms_data["Profit"].cumsum()
ms_data.tail()


# In[10]:


#plot the wealth to show the growth of profit over the period

ms_data['wealth'].plot()
plt.title('Total money you win is {}'.format(ms_data.loc[ms_data.index[-2], 'wealth']))


# ### (づ｡◕‿‿◕｡)づ
