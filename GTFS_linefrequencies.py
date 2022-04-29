#!/usr/bin/env python
# coding: utf-8

# In[221]:


get_ipython().system('pip install gtfs_functions')
get_ipython().system('pip install branca')
get_ipython().system('pip install plotly')
get_ipython().system('pip install jenkspy')
get_ipython().system('pip install keplergl')


# In[205]:


import gtfs_functions as gtfs
import branca
import pandas as pd
import geopandas as pd
import os 
import plotly.express as px
import jenkspy
import keplergl as kp


# In[206]:


routes, stops, stop_times, trips, shapes = gtfs.import_gtfs("Transit_GTFS")


# In[207]:


routes.head(4)


# In[208]:


stops.head(2)


# In[209]:


stop_times.head(3)


# In[210]:


trips.head(3)


# In[211]:


shapes.head(2)


# In[212]:


cutoffs = [0,6,9,15,19,22,24]
stop_freq = gtfs.stops_freq(stop_times, stops, cutoffs = cutoffs)


# In[213]:


stop_freq.loc[stop_freq.stop_name=='Mission St & 7th St'].sort_values(by=['dir_id','window'])


# In[214]:


cutoffs = [0,6,9,15,19,22,24]
line_freq = gtfs.lines_freq(stop_times, trips, shapes, routes, cutoffs = cutoffs)


# In[215]:


line_freq.loc[line_freq.route_name=='54 FELTON'].sort_values(by=['dir_id','window'])


# In[216]:


condition_dir = line_freq.dir_id == 'Inbound'
condition_window = line_freq.window == '6:00-9:00'

gdf = line_freq.loc[(condition_dir & condition_window),:].reset_index()

gtfs.map_gdf(gdf = gdf,
             variable = 'ntrips', 
             colors = ["#d13870", "#e895b3", "#55d992", "#3ab071", "#0e8955", "#066a40", "#066a40"],
             tooltip_var = ['route_name'] ,
             tooltip_labels = ['Route: '],
             breaks = [5,10,15,20])
        


# In[228]:


condition_dir = stop_freq.dir_id == 'Inbound'
condition_window = stop_freq.window == '6:00-9:00'

gdf = stop_freq.loc[(condition_dir & condition_window),:].reset_index()

gtfs.map_gdf(gdf = gdf,
             variable = 'ntrips', 
             colors = ["#d13870", "#e895b3", "#55d992", "#3ab071", "#0e8955", "#066a40", "#066a40"],
             tooltip_var = ['frequency'] ,
             tooltip_labels = ['Frequency: '],
             breaks = [10,20,30,40,120,200])


# In[ ]:




