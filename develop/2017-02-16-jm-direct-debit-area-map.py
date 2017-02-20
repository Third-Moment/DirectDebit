
# coding: utf-8

# ## Direct debit requires that a list of banking services be provided to employees base on:
# * Thier place of employment
# * Place of residence
# 
# This is an effort to automate the delivery of thjat information. For each employee, this script should:
# 1. Provide a list of banking services located within 1 (radial?) mile of their home address
# 2. Provide a map with the location of banking services coresponding to the list above (ennumerated?)
# 3. Provide a list of banking services located within 1 (radial?) mile of their work address
# 4. Provide a map with the location of banking services coresponding to the list above (ennumerated?)
# 
# For the purposes of this proof of concept, banking services will be defined to include:
# * Bank branches
# * ATM machines
# 
# Assumptions: 
# 1. Data will be provided in csv format
#     * to include:
#         * Name (First & Last)
#         * Home Address
#         * Office location & Address
#         

# ## Imports
# 

# In[30]:

#Imports first

import os
import matplotlib.pyplot as plt
import requests
import pandas as pd


# ## Convert home address into lat-long

# In[ ]:




# ## Convert office address into lat-long

# In[ ]:




# ## Search for banking services near home

# In[ ]:




# ## Search for banking services near office

# ####  Get API key - stored in file name: gm-config.config

# In[25]:

apikey_path = "C:/Users/Jonathan/Google Drive/"


# In[29]:

with open(apikey_path + 'gm_config.config', 'r') as f:
    api_key = f.readline()


# In[ ]:

place_type = 'atm'
near_radius = 1 # in miles
keywords = 'bank'
search_location = ''
KEY = api_key

