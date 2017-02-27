
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


# In[102]:

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


# #####  Function to create home address

# In[100]:

# Define function for getting all the needed employee details
def create_employee_home_address(data_frame, row_num): 
    home_address = ' '.join([data_frame.iloc[row_num]['NUMBER'],data_frame.iloc[row_num]['STREET'], data_frame.iloc[row_num]['CITY'],data_frame.iloc[row_num]['REGION']])
    return home_address


# In[104]:

# test create_employee_home_address function
x = create_employee_home_address(df_clean, 0)
x


# ##### Test googlemaps api...

# ####  Get API key - stored in file name: gm-config.config

# In[8]:

# get api key from file - no, github, you can't have my api key
apikey_path = "C:/Users/Jonathan/Google Drive/"
with open(apikey_path + 'gm_config.config', 'r') as f:
    api_key = f.readline()
    api_key = api_key.strip()


# In[115]:


gmaps = googlemaps.Client(key=api_key)
address = 'Constitution Ave NW & 10th St NW, Washington, DC'
lat= gmaps.geocode(address)[0]
lat


# In[83]:

lat_long = dict([])
lat['geometry']['location']
lat_long = (lat['geometry']['location']['lat'], lat['geometry']['location']['lng'])


# In[85]:

lat_long


# ##### Function to get lat-lon

# In[112]:

# Function to get lat-long as a dictionary from googlemaps api

def convert_address_to_lat_lon(address, api_key):
    gmaps = googlemaps.Client(key=api_key)
    lat = gmaps.geocode(address)[0]
    return (lat['geometry']['location']['lat'], lat['geometry']['location']['lng'])
    


# In[113]:

# Test convert_address_to_lat_lon function

y = convert_address_to_lat_lon(x, api_key)
y


# ## Convert office address into lat-long

# #####  Function to create office address

# In[105]:

# Define function for getting all the needed employee details
def create_employee_office_address(data_frame, row_num): 
    office_address = ' '.join([data_frame.iloc[row_num]['OFFICE_NUMBER'],data_frame.iloc[row_num]['OFFICE_STREET'], data_frame.iloc[row_num]['OFFICE_CITY'],data_frame.iloc[row_num]['OFFICE_REGION']])
    return office_address


# In[106]:

# test create_employee_home_address function
x = create_employee_office_address(df_clean, 0)
x


# In[ ]:




# ## Search for banking services near home

# In[10]:

place_type = 'atm'
near_radius = 1 # in miles
keywords = 'bank'
search_location = ''
KEY = api_key


# In[84]:




# In[128]:

banking_places = gmaps.places("banking services", location=lat_long, type='atm', radius=1600)


# In[126]:

banking_places


# In[33]:

banking_places.keys()


# In[34]:

print(json.dumps(banking_places['results'], indent=4))


# In[137]:

markers =[]
for bank in banking_places['results']:
    markers.append(bank['formatted_address'])
    print([bank['name'], bank['formatted_address']])
print(markers)


# #####  Create function to return banking service locations within 1 mile (1600 meters) of home address; limited to top ten results

# In[157]:

# Define function for getting banking services near home address
def find_banking_services(query, location, bank_type, radius):
    banking_places = gmaps.places(query, location=location, type=bank_type, radius=radius)
    locations =[]
    for bank in banking_places['results'][0:9]:
        locations.append([bank['name'], bank['formatted_address']])
    return locations




# In[158]:

# Test find_banking_services 
query = 'bank'
location = x  #home address reference from above
bank_type = 'atm'
radius = 1600

z = find_banking_services(query, location, bank_type, radius)
z


# In[155]:




# In[119]:

##Google maps static API can only place 10 total markers

s = "|";
markers = s.join(markers[0:9])
markers


# In[ ]:




# In[173]:

## Test bringing in package -- found a better way using report lab so commented out

# import importlib.util
# spec = importlib.util.spec_from_file_location("create_map_markers", 
#                                               "C:/Users/Jonathan/DirectDebit/src/create_map_markers.py")
# foo = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(foo)

# m=foo.Map()


# In[175]:

# m.add_point(38.8969, -77.02)


# In[240]:

# Use the next payload - is more complete

payload = {#'zoom': '13',
           'size': '400x400', 
           #'scale': '1',
           'maptype': 'roadmap',
           'markers': '435 8th St NW, Washington, DC 20004, United States|555 12th St NW, Washington, DC 20004, United States ',}


# In[120]:

#attempt at all the markers
payload = {#'zoom': '13',
           'size': '100x100', 
           #'scale': '1',
           'maptype': 'roadmap',
           'markers': markers,
    'key':api_key}


# In[121]:


r = requests.get('https://maps.googleapis.com/maps/api/staticmap?', params=payload)



# In[122]:

i = Image.open(BytesIO(r.content))
i = i.convert("RGBA")
new_img = ImageOps.expand(converted_image,border=5,fill='black')
new_img.save('C:/Users/Jonathan/DirectDebit/figures/test_image.png')

new_img


# In[61]:




# In[ ]:




# In[ ]:

def create_map_markers(:
    s = "|"
    markers = s.join(markers[0:9])
    markers


# In[50]:





# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[53]:

new_img = ImageOps.expand(converted_image,border=2,fill='black')


# In[54]:

new_img


# In[ ]:




# ## Search for banking services near office
