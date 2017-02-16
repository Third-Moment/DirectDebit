
# coding: utf-8

# Need to create a csv file of sample data to be used in direct debit map project
# Pulled only ny state address data from:
# https://openaddresses.io/
# 
# I will take a random sample of this because it's too big to store.  Plus I want to make sure that the addresses are not all from the same area.
# 
# Will also need to add some names.  Pulled names from a name generator here:
# http://homepage.net/name_generator/

# In[14]:

import pandas as pd
import random


# # Address Processing

# In[36]:

addr_file_loc = 'C:/Users/Jonathan/DirectDebit/raw_data/'
addr_file_path = file_loc + 'statewide.csv'
n = sum(1 for line in open(addr_file_path)) - 1 #number of records in file (excludes header)
s = 100
skip = sorted(random.sample(range(1,n+1),n-s))
df_addr = pd.read_csv(addr_file_path, skiprows=skip)


# In[39]:

df_addr.to_csv('address_clean.csv', sep=',')


# In[40]:

df_addr.head()


# # Name Processing

# In[45]:

name_file_loc = 'C:/Users/Jonathan/DirectDebit/data/'
name_file_path = name_file_loc + 'names_clean.csv'


# In[46]:

df_name = pd.read_csv(name_file_path)


# In[47]:

df_name.head()


# # Combine names & addresses and save to folder

# In[48]:

df_final_clean =pd.concat([df_name, df_addr], axis=1)


# In[49]:

df_final_clean.head()


# In[50]:

df_final_clean.to_csv('direct_debit_clean.csv', sep=',')

