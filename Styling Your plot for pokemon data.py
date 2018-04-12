
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pokemons = pd.read_csv(r"C:\Users\User\Documents\wine\Pokemon.csv", index_col=0)
pokemons.head(3)


# In[17]:


pokemons.plot.scatter(x = 'Attack', y = 'Defense', figsize = (12,6), title = "Pokemon by Attack and Defense")


# In[29]:


ax = pokemons['Total'].plot.hist(color = 'gray', figsize = (12,6), bins = 50, fontsize = 14)
ax.set_title("Pokemon by Stat Total", fontsize = 20)


# In[34]:


bx = pokemons['Type 1'].value_counts().plot.bar(fontsize = 14, figsize = (12,6))
bx.set_title("Pokemon by Primary Type", fontsize = 20)
sns.despine(bottom = 'True', left = 'True')

