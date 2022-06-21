
# coding: utf-8

# ## Population and Sample

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Create a Population DataFrame with 10 data 

data = pd.DataFrame()
data['Population'] = [47, 48, 85, 20, 19, 13, 72, 16, 50, 60]


# You may get different results from sampling.

# In[3]:


# Draw sample with replacement, size=5 from Population

a_sample_with_replacement = data['Population'].sample(5, replace=True)
print(a_sample_with_replacement)


# In[4]:


# Draw sample without replacement, size=5 from Population

a_sample_without_replacement = data['Population'].sample(5, replace=False)
print(a_sample_without_replacement)


# # Parameters and Statistics

# In[5]:


# Calculate mean and variance
population_mean = None
population_var = None
print('Population mean is ', population_mean)
print('Population variance is', population_var)


# **Expected Output: ** Population mean is  43.0
# Population variance is 571.8
# 

# You may get different result from sampling.

# In[6]:


# Calculate sample mean and sample standard deviation, size =10
# You will get different mean and varince every time when you excecute the below code

a_sample = data['Population'].sample(10, replace=True)
sample_mean = a_sample.mean()
sample_var = a_sample.var()
print('Sample mean is ', sample_mean)
print('Sample variance is', sample_var)


# # Average of an unbiased estimator

# In[9]:


sample_length = 500
sample_variance_collection = [data['Population'].sample(10, replace=True).var(ddof=1) for i in range(sample_length)]


# In[10]:


sample_variance_collection


# In[ ]:




