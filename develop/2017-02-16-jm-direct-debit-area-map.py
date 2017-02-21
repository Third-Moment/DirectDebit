
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

# In[177]:

#Imports first

import os
import matplotlib.pyplot as plt
import requests
import pandas as pd
from googlemaps import googlemaps
import json
from PIL import Image
from io import BytesIO


# ## Import data

# ## Convert home address into lat-long

# In[4]:

file_loc = 'C:/Users/Jonathan/DirectDebit/data/'
file_path = file_loc + 'direct_debit_clean.csv'
ouput_loc = 'C:/Users/Jonathan/DirectDebit/data/'

df_clean = pd.read_csv(file_path)


# In[5]:

df_clean.head()


# In[38]:

# Loop through all of the addresses
# for row in df_clean.iterrows():
#     print(row)
df_clean.iloc[0]


# In[44]:

df_clean.iloc[0]['NUMBER'] + df_clean.iloc[0]['STREET'] + df_clean.iloc[0]['CITY'] + df_clean.iloc[0]['REGION'].format()


# In[54]:

address = ' '.join([df_clean.iloc[0]['NUMBER'],df_clean.iloc[0]['STREET'], df_clean.iloc[0]['CITY'],df_clean.iloc[0]['REGION']])
address


# In[ ]:




# ## Convert office address into lat-long

# In[ ]:




# ## Search for banking services near home

# In[62]:

gmaps = googlemaps(api_key)


# ## Search for banking services near office

# ####  Get API key - stored in file name: gm-config.config

# In[55]:

apikey_path = "C:/Users/Jonathan/Google Drive/"


# In[91]:

with open(apikey_path + 'gm_config.config', 'r') as f:
    api_key = f.readline()
    api_key = api_key.strip()


# In[63]:

place_type = 'atm'
near_radius = 1 # in miles
keywords = 'bank'
search_location = ''
KEY = api_key


# In[88]:

from googlemaps import googlemaps
gmaps = googlemaps.Client(key=api_key)
address = 'Constitution Ave NW & 10th St NW, Washington, DC'
lat= gmaps.geocode(address)[0]
lat


# In[108]:

lat_long = dict([])
lat['geometry']['location']
lat_long = {'lat': lat['geometry']['location']['lat'], 'lon':lat['geometry']['location']['lng']}


# In[107]:

lat_long


# In[131]:

banking_places = gmaps.places("banking services", location=(38.8921037,-77.0259612), type='atm')


# In[132]:

banking_places


# In[133]:

banking_places.keys()


# In[117]:

print(json.dumps(banking_places['results'], indent=4))


# In[153]:

for bank in banking_places['results']:
     print([bank['name'], bank['formatted_address']])


# In[173]:

import importlib.util
spec = importlib.util.spec_from_file_location("create_map_markers", 
                                              "C:/Users/Jonathan/DirectDebit/src/create_map_markers.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)

m=foo.Map()


# In[175]:

m.add_point(38.8969, -77.02)


# In[240]:

payload = {#'zoom': '13',
           'size': '400x400', 
           #'scale': '1',
           'maptype': 'roadmap',
           'markers': '435 8th St NW, Washington, DC 20004, United States|555 12th St NW, Washington, DC 20004, United States ',}


# In[241]:


r = requests.get('https://maps.googleapis.com/maps/api/staticmap?', params=payload)
print(r.url)


# In[242]:

i = Image.open(BytesIO(r.content))
i


# In[211]:

get_ipython().set_next_input('https://maps.googleapis.com/maps/api/staticmap');get_ipython().magic('pinfo staticmap')
    zoom=13&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7CBrooklyn+Bridge,New+York,NY&


# In[ ]:

get_ipython().set_next_input('https://maps.googleapis.com/maps/api/staticmap');get_ipython().magic('pinfo staticmap')
    zoom=13&size=600x300&maptype=roadmap&marker=color:blue%7Clabel:S%7CBrooklyn+Bridge+New+York+NY


# In[ ]:



