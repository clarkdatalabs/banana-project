#!/usr/bin/env python
# coding: utf-8

# In[115]:


### Banana Project in Python
# Author: Cali Li
# Date: 11/1/2019
# This script is to generate a line plot about banana exportation for 11 countries during 1994-2005.
# We try to make an animation based on the data set 'banana' 
# have a clearer understanding of the banana prices in different countries and how it changes over time.

# import nassary packages
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly

# import data set as a pandas data frame
banana = pd.read_csv('FAOSTAT_data_10-18-2019.csv')
# the data range in the data set is 1993-2005
years = ["1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003",
         "2004", "2005"]


# In[105]:


# Basic informaion about the data set 'banana'
banana.info


# In[106]:


# make list of areas
Area = []
for area in banana["Area"]:
    if area not in Area:
        Area.append(area)
# 11 areas are listed below:
# 'Belgium-Luxembourg', 'Cameroon', 'Colombia', 'Costa Rica', 'Ecuador', 'Guatemala', 'Honduras', 'Panama', 'Philippines',
# 'United Arab Emirates', 'United States of America'.


# In[107]:


# make figure
fig_dict = {
    "data": [],
    "layout": {},
    "frames": []
}


# In[108]:


# we have values in $1000 USD and tonnes / etc
# using 2 data sets stores different value types
banana1=banana[banana['Unit']=='tonnes']
banana2=banana[banana['Unit']=='1000 US$']


# In[110]:


# compute the max value and the min value of 2 daa sets.
# that helps us decide the range of x and y axes.
max(banana1['Value'])
max(banana2['Value'])
min(banana1['Value'])
min(banana2['Value'])


# In[111]:


# fill in most of layout
fig_dict["layout"]["xaxis"] = {"range": [0, 4900000], "title": "Banana Values(tonnes)"}
fig_dict["layout"]["yaxis"] = {"range": [0, 1400000],"title": "Banana Values(1000 US$)"}
fig_dict["layout"]["hovermode"] = "closest"
fig_dict["layout"]["sliders"] = {
    "args": [
        "transition", {
            "duration": 400,
            "easing": "cubic-in-out"
        }
    ],
    "initialValue": "1994",
    "plotlycommand": "animate",
    "values": years,
    "visible": True
}

fig_dict["layout"]["updatemenus"] = [
    {
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 500, "redraw": False},
                                "fromcurrent": True, "transition": {"duration": 300,
                                                                    "easing": "quadratic-in-out"}}],
                "label": "Play",
                "method": "animate"
            },
            {
                "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"
            }
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 87},
        "showactive": False,
        "type": "buttons",
        "x": 0.1,
        "xanchor": "right",
        "y": 0,
        "yanchor": "top"
    }
]

sliders_dict = {
    "active": 0,
    "yanchor": "top",
    "xanchor": "left",
    "currentvalue": {
        "font": {"size": 20},
        "prefix": "Year:",
        "visible": True,
        "xanchor": "right"
    },
    "transition": {"duration": 300, "easing": "cubic-in-out"},
    "pad": {"b": 10, "t": 50},
    "len": 0.9,
    "x": 0.1,
    "y": 0,
    "steps": []
}


# In[112]:


# make data
year = 1994
for area in Area:
    dataset_by_year = banana[banana["Year"] == year]
    dataset_by_year_and_area = dataset_by_year[
        dataset_by_year["Area"] == area]
    dataset_by_year_and_area1 = dataset_by_year_and_area[
        dataset_by_year_and_area['Unit']=='tonnes']
    dataset_by_year_and_area2 = dataset_by_year_and_area[
        dataset_by_year_and_area['Unit']=='1000 US$']

    data_dict = {
        "x": list(dataset_by_year_and_area1['Value']),
        "y": list(dataset_by_year_and_area2['Value']),
        "mode": "markers",
        "text": list(dataset_by_year_and_area1["Area"]),
        "marker": {
            "sizemode": "area",
            "sizeref": 2000,
            "size": list(dataset_by_year_and_area1["Value"])
        },
        "name": area
    }
    fig_dict["data"].append(data_dict)


# In[113]:


# make frames
for year in years:
    frame = {"data": [], "name": str(year)}
    for area in Area:
        dataset_by_year = banana[banana["Year"] == int(year)]
        dataset_by_year_and_area = dataset_by_year[
            dataset_by_year["Area"] == area]
        dataset_by_year_and_area1 = dataset_by_year_and_area[
        dataset_by_year_and_area['Unit']=='tonnes']
        dataset_by_year_and_area2 = dataset_by_year_and_area[
        dataset_by_year_and_area['Unit']=='1000 US$']

        data_dict = {
            "x": list(dataset_by_year_and_area1["Value"]),
            "y": list(dataset_by_year_and_area2["Value"]),
            "mode": "markers",
            "text": list(dataset_by_year_and_area1["Area"]),
            "marker": {
                "sizemode": "area",
                "sizeref": 2000,
                "size": list(dataset_by_year_and_area1["Value"])
            },
            "name": area
        }
        frame["data"].append(data_dict)

    fig_dict["frames"].append(frame)
    slider_step = {"args": [
        [year],
        {"frame": {"duration": 300, "redraw": False},
         "mode": "immediate",
         "transition": {"duration": 300}}
    ],
        "label": year,
        "method": "animate"}
    sliders_dict["steps"].append(slider_step)


# In[116]:


fig_dict["layout"]["sliders"] = [sliders_dict]

# draw the scatter plot
fig = go.Figure(fig_dict)
# save the plot as a html file
plotly.offline.plot(fig, filename = 'animation.html', auto_open=False)
# show it inline
fig.show()


# In[ ]:




