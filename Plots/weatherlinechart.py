import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
new_df = df.groupby(['month']).agg({'actual_max_temp': 'max'}).reset_index()

# Preparing data
# The data collects the dates and what number is recorded for the Confirmed category
# It scatters the data on the graph and connects it through a line
data = [go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'],
                   mode='lines', name='Temperature')]
# Preparing layout
layout = go.Layout(title='Max Temperature By Month', xaxis_title="Month",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weatherlinechart.html')