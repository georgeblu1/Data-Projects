
# coding: utf-8

# In[3]:


import pandas as pd
reviews = pd.read_csv(r"C:\Users\User\Documents\wine\wine150k.csv", index_col=0)
reviews.head(3)


# In[12]:


reviews['points'].value_counts().sort_index().plot.bar(figsize=(12,6), 
                                                       color = 'mediumvioletred', 
                                                       fontsize = 16, 
                                                       title = 'Ranking given by wine magazine'
                                                      ) #simple tweaking to make the graphs prettier


# In[15]:


import matplotlib.pyplot as plt
ax = reviews['points'].value_counts().sort_index().plot.bar(figsize = (12,6),
                                                           color = 'mediumvioletred',
                                                           fontsize = 16)
ax.set_title('Rankings given by wine magazine', fontsize = 20)

# above shows when the plots are done using matplotlib whereby the title can be changed. After that we will use Seaborn and remove the black border ewww
# In[17]:


import matplotlib.pyplot as plt
import seaborn as sns
ax = reviews['points'].value_counts().sort_index().plot.bar(figsize = (12,6),
                                                           color = 'mediumvioletred',
                                                           fontsize = 16)
ax.set_title('Rankings given by wine magazine', fontsize = 20)
sns.despine(bottom= True, left = True)

