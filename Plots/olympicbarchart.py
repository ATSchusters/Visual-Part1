import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
from Plots.barchart import data

df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Creating sum of number of cases group by Country Column
new_df = df.groupby(['NOC']).agg(
    {'Gold': 'sum', 'Silver': 'sum', 'Bronze': 'sum', 'Total':
     'sum'}).reset_index()
# Sorting values and select 20 first value
new_df = new_df.sort_values(by=['Total'], ascending=[False]).head(20).reset_index()

# Preparing data
data = go.Bar(x=new_df['NOC'], y=new_df['Total'], name='Number of Medals',
                marker={'color': '#156CED'})

# Preparing layout
layout = go.Layout(title='Top 20 Countries of The 2016 Olympics',
                   xaxis_title="Country", yaxis_title="Number of Medals",
                   showlegend=True)
# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='olympicbarchart.html')