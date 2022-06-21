
# coding: utf-8

# # Diagnostic of models

# In[1]:


import pandas as pd 
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:


housing = pd.DataFrame.from_csv('../data/housing.csv')
housing.head()


# In[3]:


model = smf.ols(formula='MEDV~LSTAT', data=housing).fit()

# Here are estimated intercept and slope by least square estimation 
b0_ols = model.params[0]
b1_ols = model.params[1]

housing['BestResponse'] = b0_ols + b1_ols*housing['LSTAT']


# # Assumptions behind linear regression model
# 1. Linearity 
# 2. independence
# 3. Normality
# 4. Equal Variance

# ## Linearity

# In[4]:


# you can check the scatter plot to have a fast check
housing.plot(kind='scatter', x='LSTAT', y='MEDV', figsize=(10, 10), color='g')


# # Independence

# In[5]:


# Get all errors (residuals)
housing['error'] = housing['MEDV'] - housing['BestResponse']


# In[6]:


# Method 1: Residual vs order plot
# error vs order plot (Residual vs order) as a fast check 
plt.figure(figsize=(15, 8))
plt.title('Residual vs order')
plt.plot(housing.index, housing['error'], color='purple')
plt.axhline(y=0, color='red')
plt.show()


# In[7]:


# Method 2: Durbin Watson Test
# Check the Durbin Watson Statistic
# Rule of thumb: test statistic value in the range of 1.5 to 2.5 are relatively normal
model.summary()


# # Normality

# In[8]:


import scipy.stats as stats
z = (housing['error'] - housing['error'].mean())/housing['error'].std(ddof=1)

stats.probplot(z, dist='norm', plot=plt)
plt.title('Normal Q-Q plot')
plt.show()


# # Equal variance

# In[9]:


# Residual vs predictor plot
housing.plot(kind='scatter', x='LSTAT', y='error', figsize=(15, 8), color='green')
plt.title('Residual vs predictor')
plt.axhline(y=0, color='red')
plt.show()


# ## We can see that the regression model (MEDV~LSTAT) violates all four assumptions. Therefore, we cannot make statistical inference using this model.
