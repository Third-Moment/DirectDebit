
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

# In[48]:

#Imports first

import os
import matplotlib.pyplot as plt
import requests
import pandas as pd
from googlemaps import googlemaps
import json
from PIL import Image, ImageOps
from io import BytesIO


# ## Import data

# ## Convert home address into lat-long

# In[3]:

file_loc = 'C:/Users/Jonathan/DirectDebit/data/'
file_path = file_loc + 'direct_debit_clean.csv'
ouput_loc = 'C:/Users/Jonathan/DirectDebit/data/'

df_clean = pd.read_csv(file_path)


# In[4]:

df_clean.head()


# In[5]:

# Loop through all of the addresses
# for row in df_clean.iterrows():
#     print(row)
df_clean.iloc[0]


# In[6]:

df_clean.iloc[0]['NUMBER'] + df_clean.iloc[0]['STREET'] + df_clean.iloc[0]['CITY'] + df_clean.iloc[0]['REGION'].format()


# In[54]:

address = ' '.join([df_clean.iloc[0]['NUMBER'],df_clean.iloc[0]['STREET'], df_clean.iloc[0]['CITY'],df_clean.iloc[0]['REGION']])
address


# In[ ]:




# ## Convert office address into lat-long

# In[ ]:




# ## Search for banking services near home

# In[ ]:




# ## Search for banking services near office

# ####  Get API key - stored in file name: gm-config.config

# In[8]:

apikey_path = "C:/Users/Jonathan/Google Drive/"


# In[9]:

with open(apikey_path + 'gm_config.config', 'r') as f:
    api_key = f.readline()
    api_key = api_key.strip()


# In[10]:

place_type = 'atm'
near_radius = 1 # in miles
keywords = 'bank'
search_location = ''
KEY = api_key


# In[11]:

from googlemaps import googlemaps
gmaps = googlemaps.Client(key=api_key)
address = 'Constitution Ave NW & 10th St NW, Washington, DC'
lat= gmaps.geocode(address)[0]
lat


# In[12]:

lat_long = dict([])
lat['geometry']['location']
lat_long = {'lat': lat['geometry']['location']['lat'], 'lon':lat['geometry']['location']['lng']}


# In[13]:

lat_long


# In[31]:

banking_places = gmaps.places("banking services", location=(38.8921037,-77.0259612), type='atm', radius=1600)


# In[32]:

banking_places


# In[33]:

banking_places.keys()


# In[34]:

print(json.dumps(banking_places['results'], indent=4))


# In[35]:

markers =[]
for bank in banking_places['results']:
    markers.append(bank['formatted_address'])
    print([bank['name'], bank['formatted_address']])


# In[36]:

##Google maps static API can only place 10 total markers

s = "|";
markers = s.join(markers[0:9])
markers


# In[ ]:




# In[ ]:




# In[ ]:




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


# In[58]:

#attempt at all the markers
payload = {#'zoom': '13',
           'size': '100x100', 
           #'scale': '1',
           'maptype': 'roadmap',
           'markers': markers,
    'key':api_key}


# In[59]:


r = requests.get('https://maps.googleapis.com/maps/api/staticmap?', params=payload)



# In[64]:

i = Image.open(BytesIO(r.content))
i = i.convert("RGBA")
new_img = ImageOps.expand(converted_image,border=5,fill='black')
new_img.save('C:/Users/Jonathan/DirectDebit/figures/test_image.png')

new_img


# In[61]:




# In[46]:




# In[ ]:

def create_map_markers(:
    s = "|"
    markers = s.join(markers[0:9])
    markers


# In[50]:





# In[53]:

new_img = ImageOps.expand(converted_image,border=2,fill='black')


# In[54]:

new_img


# In[ ]:

print

