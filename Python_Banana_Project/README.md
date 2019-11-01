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

## import necessary packages

### pandas is a way to import data set

```
import pandas as pd
```

### plotly package to help us export plot

```
import plotly
```
### plotly.express helps to generate the plot

```
import plotly.express as px
```

## data processing

### input data set as a data frame using pandas
```
banana = pd.read_csv('FAOSTAT_w_Belgium_Lux_Post_2000.csv')
```

### filter the data set
```
banana=banana[banana['Unit']=='tonnes']
```

## plot

### generate line plot
```
fig = px.line(banana, x="Year", y="Value", color="Area")
```
### export plot
```
plotly.offline.plot(fig, filename = 'line chart.html', auto_open=False)
```

### show the plot
```
fig.show()
```
