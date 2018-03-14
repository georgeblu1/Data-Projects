
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
pd.set_option('max_columns', None)
pokemon = pd.read_csv(r"C:\Users\George\Documents\biodiversity-in-national-parks\pokemon.csv")
pokemon.head(3)


# In[4]:


pokemon['type1'].value_counts().head(18).plot.bar()


# In[9]:


pokemon['hp'].value_counts().sort_index().plot.line()


# In[11]:


pokemon['weight_kg'].plot.hist()

