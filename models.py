# math operations
# import math
# produce random numbers
# import random
# to load json files
import json
# datetime operations
from datetime import timedelta
# to get web contents
# from urllib.request import urlopen

# for numerical analyiss
import numpy as np
# to store and process data in dataframe
import pandas as pd

# basic visualization package
import matplotlib.pyplot as plt
# advanced ploting
import seaborn as sns

# interactive visualization
import plotly.express as px
import plotly.graph_objects as go
import plotly
# import plotly.figure_factory as ff
from plotly.subplots import make_subplots

# for offline ploting
# from plotly.offline import plot, iplot, init_notebook_mode

# init_notebook_mode(connected=True)

# converter
# from pandas.plotting import register_matplotlib_converters
# register_matplotlib_converters()

# hide warnings
import warnings

warnings.filterwarnings('ignore')

# to USA states details
# import us

# color pallette
cnf, dth, rec, act = '#ffbf47', '#6f0000', '#0f9b0f', '#1cb5e0'


def fullData(url):
    full_table = pd.read_csv(url)


def groupedData(url):
    grouped_table = pd.read_csv(url)
    grouped_table['Date'] = pd.to_datetime(grouped_table['Date'])


def ratio_dayWise(url):
    day_wise = pd.read_csv(url)
    day_wise['Date'] = pd.to_datetime(day_wise['Date'])
    temp = day_wise[['Date', 'Deaths', 'Recovered', 'Active']].tail(1)
    temp = temp.melt(id_vars='Date', value_vars=['Active', 'Deaths', 'Recovered'])
    fig = [
        go.Treemap(temp, path=['variable'], values='value', height=225, color_discrete_sequence=[act, rec, dth])
    ]
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphJSON)
    # return graphJSON


def case_over_time_map(url, col, title):
    df = pd.read_csv(url)

    fig = [go.Choropleth(locations=df['Country/Region'],
                         z=df[col].astype(float),
                         locationmode='country names',
                         colorbar_title=title,
                         text=df['Country/Region'],
                         reversescale=True,
                         marker_line_width=0.5).update(autocolorscale=True,
                                                       hovertemplate=df['Deaths'])]
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def plot_daywise_bar(url):
    df = pd.read_csv(url)
    date = pd.to_datetime(df['Date'])
    fig = [go.Bar(x=date, y=df['Confirmed'], name='Confirmed'),
           go.Bar(x=date, y=df['New cases'], name='New Cases'),
           go.Bar(x=date, y=df['Deaths'], name='Deaths'),
           go.Bar(x=date, y=df['Active'], name='Active'),
           go.Bar(x=date, y=df['Recovered'], name='Recovered'),
           go.Bar(x=date, y=df['New recovered'], name='New recovered'),
           go.Figure().update_layout(barmode='stack', title='Day Wise COVID Spread')
           ]
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def plot_daywise_line(url):
    df = pd.read_csv(url)
    date = pd.to_datetime(df['Date'])
    fig = [go.Line(x=date, y=df['New cases'], mode='lines', name='New cases'),
           go.Line(x=date, y=df['Confirmed'], mode='lines', name='Confirmed'),
           go.Line(x=date, y=df['Deaths'], name='Deaths'),
           go.Line(x=date, y=df['Active'], name='Active'),
           go.Line(x=date, y=df['Recovered'], name='Recovered'),
           go.Line(x=date, y=df['New recovered'], name='New recovered'),
           go.Figure().update_layout(title='Day Wise COVID Spread', xaxis_title="", yaxis_title="")]
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def top_twenty_hbar(url, col, n, hover_data=[]):
    df = pd.read_csv(url)
    df = df.sort_values(col).tail(n)
    fig = [go.Bar(x=df[col],
                  y=df['Country/Region'],
                  hovertext=hover_data,
                  orientation='h',
                  marker_color=df[col]
                  )]
    graphJson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJson


def plot_hbar_wm(url, col, n, min_pop=1000000):
    df = pd.read_csv(url)
    df = df[df['Population'] > min_pop]
    df = df.sort_values(col, ascending=True).tail(n)
    fig = [go.Bar(
        x=df[col],
        y=df['Country/Region'],
        marker_color=df[col],
        orientation='h',
        text=col + '(Only Countries with > 1M Population)'
    )]

    graphJson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJson

