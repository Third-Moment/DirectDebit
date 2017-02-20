
# coding: utf-8

# Need to create a csv file of sample data to be used in direct debit map project
# Pulled only ny state address data from:
# https://openaddresses.io/
# 
# I will take a random sample of this because it's too big to store.  Plus I want to make sure that the addresses are not all from the same area.
# 
# Will also need to add some names.  Pulled names from a name generator here:
# http://homepage.net/name_generator/

# In[34]:

import pandas as pd
import random


# # Address Processing

# In[35]:

addr_file_loc = 'C:/Users/Jonathan/DirectDebit/raw_data/'
addr_file_path = addr_file_loc + 'statewide.csv'
ouput_loc = 'C:/Users/Jonathan/DirectDebit/data/'

n = sum(1 for line in open(addr_file_path)) - 1 #number of records in file (excludes header)
s = 100
skip = sorted(random.sample(range(1,n+1),n-s))
df_addr = pd.read_csv(addr_file_path, skiprows=skip)


# In[36]:

df_addr.to_csv(ouput_loc + 'address_clean.csv', sep=',')


# In[37]:

df_addr.head()


# # Name Processing

# In[38]:

name_file_loc = 'C:/Users/Jonathan/DirectDebit/data/'
name_file_path = name_file_loc + 'names_clean.csv'


# In[39]:

df_name = pd.read_csv(name_file_path)


# In[40]:

df_name.head()


# ## Office location processing

# In[43]:

office_file_loc = 'C:/Users/Jonathan/DirectDebit/raw_data/'
office_file_path = office_file_loc + 'statewide.csv'
n = sum(1 for line in open(addr_file_path)) - 1 #number of records in file (excludes header)
s = 100
skip = sorted(random.sample(range(1,n+1),n-s))
df_office = pd.read_csv(office_file_path, skiprows=skip)


# In[44]:

list(df_office)


# In[45]:

df_office = df_office[["NUMBER", "STREET", "CITY", "POSTCODE"]]
df_office.columns = ["OFFICE_NUMBER", "OFFICE_STREET", "OFFICE_CITY", "OFFICE_POSTCODE"]
df_office.head()


# # Combine names, addresses, and office locations and save to folder

# In[47]:

df_final_clean =pd.concat([df_name, df_addr, df_office], axis=1)


# In[48]:

df_final_clean.head()


# In[49]:

ouput_loc = 'C:/Users/Jonathan/DirectDebit/data/'
df_final_clean.to_csv(ouput_loc + 'direct_debit_clean.csv', sep=',')

