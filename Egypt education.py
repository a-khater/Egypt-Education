#!/usr/bin/env python
# coding: utf-8

# In[67]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Open file and specify Egypt

# In[110]:


df = pd.read_excel("D:\datasets\Education-Egypt-Data Set.xls" , header=1 , index_cols=False ,sheet_name='Egypt Data' )


# In[114]:


xl = df.loc[df['Country Code'] =='EGY']


# In[119]:


x = ["Country Name" , "Country Code" , "Indicator Code"]


# In[122]:


xn = xl.drop(x , axis=1)


# In[129]:


xn.index = range(len(xn))


# Plots

# In[274]:


for x in range(len(xn)) :
    l=xn.iloc[x:x+1,:]
    o = l[['Indicator Name']]
    w = str(o)
    z=l.melt()
    z=z.iloc[1:,:2]
    z.index = z['variable']
    z['value'].plot()
    plt.title(w)

    plt.show()


# In[ ]:




