import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
new_df = df.groupby(['month']).agg(
    {'actual_mean_temp': 'mean', 'actual_min_temp': 'min',
     'actual_max_temp': 'max'}).reset_index()

# Preparing data
# The data collects the dates and what number is recorded for the Confirmed category
# It scatters the data on the graph and connects it through a line
trace1 = go.Scatter(x=new_df['month'], y=new_df['actual_mean_temp'],
                     mode='lines', name='mean')
trace2 = go.Scatter(x=new_df['month'], y=new_df['actual_min_temp'],
                     mode='lines', name='min')
trace3 = go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'],
                     mode='lines', name='max')
data = [trace1, trace2, trace3]
# Preparing layout
layout = go.Layout(title='Multi Line Chart of Max, Mean, and Min Temperature', xaxis_title="Month",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weathermultilinechart.html')