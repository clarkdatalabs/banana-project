#!/usr/bin/env python
# coding: utf-8

# In[35]:


### Banana Project in Python
# Author: Cali Li
# Date: 11/1/2019
# This script is to generate a line plot about banana exportation for 11 countries during 1993-2005.
# We try to make a 2-dim clear and explicit line plot to analysis data.

## import necessary packages
# pandas is a way to import data set
import pandas as pd
# plotly package to help us export plot
import plotly
# plotly.express helps to generate the plot
import plotly.express as px

#$ data processing
# input data set as a data frame using pandas
banana = pd.read_csv('FAOSTAT_w_Belgium_Lux_Post_2000.csv')
# filter the data set
banana=banana[banana['Unit']=='tonnes']

## plot
# generate line plot
fig = px.line(banana, x="Year", y="Value", color="Area")
# export plot
plotly.offline.plot(fig, filename = 'line chart.html', auto_open=False)
# show the plot
fig.show()


# In[ ]:




