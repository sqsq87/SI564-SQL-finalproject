#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
a=pd.read_csv('SI564/NYPD_Shooting_Incident_Data__Historic_.csv')


# In[48]:


index=[]
for i in range(len(a)):
    if (a.loc[i]['OCCUR_DATE'][6:10]=='2019' ) and (a.loc[i]['OCCUR_DATE'][0:2]<='06' ):
        index.append(i)


# In[49]:


a_2019=a.loc[index]


# In[56]:


a_2019['is_murder']=a_2019['STATISTICAL_MURDER_FLAG'].map({True:1,False:0})


# In[64]:


a_2019['OCCUR_DATETIME']=a_2019['OCCUR_DATE']+' '+ a_2019['OCCUR_TIME']


# In[65]:


a_2019


# In[68]:


a_2019.to_csv('SI564/shooting_2019.csv', index=False)


# In[ ]:




