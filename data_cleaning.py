#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# In[43]:


def clean_cad_data(filepath):
    
    cad = pd.read_csv(filepath)
    
    cad = cad.dropna(subset=['Nature Code'])
    
    columns_to_drop = [
    'Seconds to Enroute', 'Seconds to Arrive', 'Seconds to Transport', 'Seconds to Last Unit Clear',
    'Seconds to Route', 'Seconds to Finish', 'Seconds to Dispatch', 'Seconds Dispatched to Arrived',
    'Seconds Dispatched to Enroute', 'Seconds Arrived to Last Unit Clear', 'Seconds Arrive to Transport',
    'Hold Time', 'Seconds Finished to Dispatched', 'Full City', 'Time Ready', 'First Transport Timestamp'
]

    # Drop all specified columns in one line
    cad = cad.drop(columns=columns_to_drop)
    
    cad['Contains_CAHOOTS'] = cad['Full Nature Code Description'].apply(lambda x: 'CAHOOTS' in str(x))
    
    return cad 


# In[44]:


def clean_cahoots_data(filepath):
    # Load the data
    cahoots = pd.read_csv(filepath)
    
    # Drop rows where 'Date' or 'TimeOfCall' is NaN
    cahoots = cahoots.dropna(subset=['Date', 'TimeOfCall'])
    
    # Convert 'Date' to datetime.date
    cahoots.loc[:, 'Date'] = pd.to_datetime(cahoots['Date'], errors='coerce').dt.date
    
    # Convert 'TimeOfCall' to datetime.time
    cahoots.loc[:, 'TimeOfCall'] = pd.to_datetime(cahoots['TimeOfCall'], errors='coerce', format='%H:%M:%S').dt.time
    
    # Drop rows where 'Date' or 'TimeOfCall' conversion resulted in NaT/NaN
    cahoots.dropna(subset=['Date', 'TimeOfCall'], inplace=True)
    
    # Combine 'Date' and 'TimeOfCall' into a single 'DateTime' column
    cahoots['DateTime'] = cahoots.apply(lambda row: pd.Timestamp.combine(row['Date'], row['TimeOfCall']), axis=1)
    
    # Drop the original 'Date' and 'TimeOfCall' columns
    cahoots.drop(columns=['Date', 'TimeOfCall'], inplace=True)
    
    return cahoots


# In[ ]:




