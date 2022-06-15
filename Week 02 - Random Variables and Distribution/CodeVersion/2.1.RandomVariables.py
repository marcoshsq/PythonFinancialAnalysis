
# coding: utf-8

# ## Outcomes and Variables

# In[3]:


#import numpy and pandas package
import numpy as np
import pandas as pd


# ### Mimic the roll dice game

# In[4]:


# roll two dice for multiple times
die = pd.DataFrame([1, 2, 3, 4, 5, 6])
sum_of_dice = die.sample(2, replace=True).sum().loc[0]
print('Sum of dice is', sum_of_dice)  

# you may get different outcomes as we now mimic the result of rolling 2 dice, but the range must be limited between 2 and 12. 


# In[5]:


# It is your turn! let's replace the none with the code of rolling three dice, instead of two

np.random.seed(1)  # This is for checking answer, do NOT modify this line of code

#Modify the code, replace the None
sum_of_three_dice = die.sample(3, replace=True).sum().loc[0]


# In[6]:


print('Sum of three dice is', sum_of_three_dice)


# **Expected output: ** Sum of three dice is 15

# ### Mimic the roll dice game for multiple times

# In[7]:


# The following code mimics the roll dice game for 50 times. And the results are all stored into "Result"
# Lets try and get the results of 50 sum of faces.

trial = 50
result = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]


# In[8]:


#print the first 10 results
print(result[:10])


# ## ヽ(o＾▽＾o)ノ
