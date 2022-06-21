
# coding: utf-8

# # Confidence Interval

# In[1]:


import pandas as pd
import numpy as np
from scipy.stats import norm


# In[2]:


ms = pd.DataFrame.from_csv('../data/microsoft.csv')
ms.head()


# ## Estimate the average stock return with 90% Confidence Interval

# In[6]:


# we will use log return for average stock return of Microsoft

ms['logReturn'] = np.log(ms['Close'].shift(-1)) - np.log(ms['Close'])


# In[9]:


# Lets build 90% confidence interval for log return
sample_size = ms['logReturn'].shape[0]
sample_mean = ms['logReturn'].mean()
sample_std = ms['logReturn'].std(ddof=1) / sample_size**0.5

# left and right quantile
z_left = norm.ppf(0.05)
z_right = norm.ppf(0.95)

# upper and lower bound
interval_left = sample_mean + z_left * sample_std
interval_right = sample_mean + z_right * sample_std


# In[10]:


# 90% confidence interval tells you that there will be 90% chance that the average stock return lies between "interval_left"
# and "interval_right".

print('90% confidence interval is ', (interval_left, interval_right))


# ** Expected output: ** 90% confidence interval is  (-1.5603253899378836e-05, 0.001656066226145423)
