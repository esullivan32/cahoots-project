#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


from data_cleaning import clean_cad_data


# In[7]:


cad = clean_cad_data("call_data_from_CAD_2022(Call Summary)_raw.csv")


# In[10]:


cad_subset = cad[['Incident Call Time', 'Full Nature Code Description', 'Contains_CAHOOTS']]
cad_subset



# Convert 'Incident Call Time' to datetime format with explicit format specification
cad['Incident Call Time'] = pd.to_datetime(cad['Incident Call Time'], format='%m/%d/%y %H:%M:%S.%f')

# Group by week and calculate proportions
cad['Week'] = cad['Incident Call Time'].dt.to_period('W')
proportions_per_week = cad.groupby('Week')['Contains_CAHOOTS'].agg(['count', 'sum'])
proportions_per_week['Proportion'] = proportions_per_week['sum'] / proportions_per_week['count']

# Display the result
print(proportions_per_week)


overall_proportion = cad['Contains_CAHOOTS'].sum() / len(cad)


print("\nOverall Proportion for all Data:", overall_proportion)

from scipy.stats import chi2_contingency

# Create contingency table for observed counts
observed_counts = proportions_per_week[['sum', 'count']].values

# Perform chi-square test
chi2_stat, p_val, _, _ = chi2_contingency(observed_counts)

print("Chi-square statistic:", chi2_stat)
print("P-value:", p_val)


import pandas as pd

# Given data
data = [
    ['2022-08-01/2022-08-07', 584, 377, 0.645548],
    ['2022-08-08/2022-08-14', 520, 297, 0.571154],
    ['2022-08-15/2022-08-21', 534, 354, 0.662921],
    ['2022-08-22/2022-08-28', 566, 353, 0.623675],
    ['2022-08-29/2022-09-04', 579, 342, 0.590674],
    ['2022-09-05/2022-09-11', 535, 329, 0.614953],
    ['2022-09-12/2022-09-18', 553, 345, 0.623870],
    ['2022-09-19/2022-09-25', 515, 319, 0.619417],
    ['2022-09-26/2022-10-02', 537, 304, 0.566108],
    ['2022-10-03/2022-10-09', 571, 343, 0.600701],
    ['2022-10-10/2022-10-16', 547, 333, 0.608775],
    ['2022-10-17/2022-10-23', 529, 316, 0.597353],
    ['2022-10-24/2022-10-30', 483, 298, 0.616977],
    ['2022-10-31/2022-11-06', 473, 287, 0.606765],
    ['2022-11-07/2022-11-13', 545, 350, 0.642202],
    ['2022-11-14/2022-11-20', 544, 353, 0.648897],
    ['2022-11-21/2022-11-27', 488, 319, 0.653689],
    ['2022-11-28/2022-12-04', 455, 292, 0.641758],
    ['2022-12-05/2022-12-11', 486, 306, 0.629630],
    ['2022-12-12/2022-12-18', 463, 281, 0.606911],
    ['2022-12-19/2022-12-25', 516, 337, 0.653101],
    ['2022-12-26/2023-01-01', 469, 281, 0.599147],
    ['2023-01-02/2023-01-08', 470, 285, 0.606383],
    ['2023-01-09/2023-01-15', 260, 71, 0.273077]
]



# In[11]:


import seaborn as sns
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))

sns.set_palette(palette='Blues')

sns.barplot(data=df, x="Week", y="Proportion", color='lightblue')
plt.xticks([]) 

plt.show()



# In[ ]:




