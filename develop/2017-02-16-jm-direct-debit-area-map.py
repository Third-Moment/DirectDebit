
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


# In[214]:

df_clean.head()


# In[193]:

for row in df_clean:
    home_address = df_clean.NUMBER + " " + df_clean.STREET + " " + df_clean.CITY + " " + df_clean.REGION
    print(home_address)


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

# In[228]:

# Define function for getting all the needed employee details
def create_employee_home_address(data_frame): 
    address = ' '.join([data_frame.iloc[row]['NUMBER'],data_frame.iloc[row]['STREET'], data_frame.iloc[row]['CITY'],data_frame.iloc[row]['REGION']])
    address


# In[231]:

# test create_employee_home_address function
for row in df_clean:
    name = df_clean.First_name + " " + df_clean.Last_name
    print(name)
df_clean.


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


# In[254]:

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




# In[232]:

banking_places = gmaps.places("banking services", location=lat_long, type='atm', radius=1600)


# In[253]:

banking_places


# In[234]:

banking_places.keys()


# In[34]:

print(json.dumps(banking_places['results'], indent=4))


# In[252]:

markers =[]
for bank in banking_places['results']:
    markers.append(bank['formatted_address'])
    print([bank['name'], bank['formatted_address']])
print(markers)


# #####  Create function to return banking service locations within 1 mile (1600 meters) of home address; limited to top ten results

# In[248]:

# Define function for getting banking services near home address
def find_banking_services(query, location, bank_type, radius):
    banking_places = gmaps.places(query, location=location, type=bank_type, radius=radius)
    locations =[]
    for bank in banking_places['results'][0:9]:
        locations.append([bank['name'], bank['formatted_address']])
    return locations




# In[256]:

# Test find_banking_services 
query = 'bank'
location = y  #home address reference from above
bank_type = 'atm'
radius = 1600

z = find_banking_services(query, location, bank_type, radius)
z


# In[155]:




# In[159]:

##Google maps static API can only place 10 total markers

s = "|";
markers = s.join(markers[0:9])
markers


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


# In[164]:

# function for converting banking services near an address to a list of markers to be plotted
def create_map_markers(marker_address_list):
    s = "|"
    return s.join(marker_address_list)


# In[257]:

# test create_map_markers function
aa = [bank[1] for bank in z]
bb = create_map_markers(aa)
bb


# In[179]:




# In[258]:

#attempt at all the markers
payload = {#'zoom': '13',
           'size': '400x400', 
           #'scale': '1',
           'maptype': 'roadmap',
           'markers': bb,
    'key':api_key}


# In[259]:


r = requests.get('https://maps.googleapis.com/maps/api/staticmap?', params=payload)



# In[260]:

i = Image.open(BytesIO(r.content))
i = i.convert("RGBA")
new_img = ImageOps.expand(converted_image,border=5,fill='black')
new_img.save('C:/Users/Jonathan/DirectDebit/figures/test_image.png')

new_img


# #####  Create function to return google map as png from banking services near address

# In[240]:

# Define function that takes a list of markers and outputs a formatted map

def create_map_with_markers(markers, api_key):
    payload = {'size': '400x400', 
           'maptype': 'roadmap',
           'markers': markers,
               'key':api_key}
    r = requests.get('https://maps.googleapis.com/maps/api/staticmap?', params=payload)
    i = Image.open(BytesIO(r.content))
    converted_image = i.convert("RGBA")
    return ImageOps.expand(converted_image,border=5,fill='black')


# In[241]:

# test create_map_with_markers function

cc = create_map_with_markers(bb, api_key)
cc


# In[50]:




# ## Generate PDFs based on bank locations and maps

# In[ ]:




# In[ ]:




# In[ ]:




# In[53]:




# In[ ]:




# In[ ]:




# In[ ]:




# ## Search for banking services near office
