# Run and Setup Python Project

## Build 
Install virtual environment library
```
cd python/
pip install virtualenv #if you don't have virtualenv installed 
```

Create virtualenv
```
virtualenv <Name_of_Virtual_Environment>
```

Activate virtualenv
```
source <Name_of_Virtual_Environment>/bin/activate
```

Install project requirements usings the requirements.text
```
pip install -r requirements.txt
```

## Run
Run python script in root directory to start
```
python app.py
```

# Python script

## Import necessary packages

pandas is a way to import data set

```
import pandas as pd
```

plotly package to help us export plot

```
import plotly
```
plotly.express helps to generate the plot

```
import plotly.express as px
```

## Data processing

Input data set as a data frame using pandas
```
banana = pd.read_csv('FAOSTAT_w_Belgium_Lux_Post_2000.csv')
```

Filter the data set
```
banana=banana[banana['Unit']=='tonnes']
```

## Plot

Generate line plot
```
fig = px.line(banana, x="Year", y="Value", color="Area")
```
Export plot
```
plotly.offline.plot(fig, filename = 'line chart.html', auto_open=False)
```

Show the plot
```
fig.show()
```

Customrize the color of those lines can make the plot become more readable. Just as the 'line chart_by group' plot shows.

# Python script for animation over time

This script is to generate a line plot about banana exportation for 11 countries during 1994-2005.

We try to make an animation based on the data set 'banana', have a clearer understanding of the banana prices in different countries and how it changes over time.

## Import nassary packages
```
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly
```

## Import data set as a pandas data frame
```
banana = pd.read_csv('FAOSTAT_data_10-18-2019.csv')
```
The data range in the data set is 1993-2005
```
years = ["1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003",
         "2004", "2005"]
```
Basic informaion about the data set 'banana'
```
banana.info
```

## Make list of areas
```
Area = []
for area in banana["Area"]:
    if area not in Area:
        Area.append(area)
```

11 areas are listed below: 'Belgium-Luxembourg', 'Cameroon', 'Colombia', 'Costa Rica', 'Ecuador', 'Guatemala', 'Honduras', 'Panama', 'Philippines', 'United Arab Emirates', 'United States of America'.

We have values in $1000 USD and tonnes / etc. We use 2 data sets stores different value types
```
banana1=banana[banana['Unit']=='tonnes']
banana2=banana[banana['Unit']=='1000 US$']
```

Compute the max value and the min value of 2 data sets, which could helps us decide the range of x and y axes.
```
max(banana1['Value'])
max(banana2['Value'])
min(banana1['Value'])
min(banana2['Value'])
```

## Make figure
```
fig_dict = {
    "data": [],
    "layout": {},
    "frames": []
}
```

Fill in most of layout
```
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
```
## Make data
```
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
 ```
 ## Make frames
 ```
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
    
fig_dict["layout"]["sliders"] = [sliders_dict]
```
Draw the scatter plot
```
fig = go.Figure(fig_dict)
```
Save the plot as a html file named 'animation'
```
plotly.offline.plot(fig, filename = 'animation.html', auto_open=False)
```
Show it inline
```
fig.show()
```
