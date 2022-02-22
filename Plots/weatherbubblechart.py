import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
new_df = df.groupby(['month']).agg(
    {'average_min_temp': 'mean',
     'average_max_temp': 'mean'}).reset_index()

# Preparing data

data = [
    go.Scatter(x=new_df['average_min_temp'],
               y=new_df['average_max_temp'],
               text=new_df['month'],
               mode='markers',
               marker=dict(size=new_df['average_max_temp'],color=new_df['average_max_temp'], showscale=True))
]
# Preparing layout
layout = go.Layout(title='Bubble Chart of The Average Min and Max Temperatures by Month', xaxis_title="Min Temperature",
                   yaxis_title="Max Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weatherbubblechart.html')