import dash_core_components as dcc
import plotly.offline as pyo
import plotly.graph_objs as go
from mra.run_data import RunData
import numpy as np
import datetime


list_of_runs = RunData.accepted_run
first_run_key = list(list_of_runs.keys())[0]


def drop_down_select_run(element_id):
    drop_down_select_run = dcc.Dropdown(
        id=element_id,
        options=[{'label': run['fullname'],
                  'value': key}
                 for key, run in list_of_runs.items()],
        value=first_run_key
    )
    return drop_down_select_run


def radio_sex(element_id):
    radio_dcc = dcc.RadioItems(
        id=element_id,
        options=[
            {'label': 'Kobieta', 'value': 'W'},
            {'label': 'Mężczyzna', 'value': 'M'},

        ],
        value='W'
    )
    return radio_dcc


def slider_year_old(element_id):
    slider = dcc.Slider(
        id=element_id,
        min=16,
        max=90,
        marks={i: '{}'.format(i) for i in range(16, 91, 2)},
        value=38,
    )
    return slider


def slider_best10(element_id):
    slider = dcc.Slider(
        id=element_id,
        min=50,
        max=150,
        marks={round(i, 2): float_to_time(i / 100)
               for i in range(5, 150, 5)},
        value=100,
    )
    return slider


def scatter(x, y, title, x_label, y_label, prediction_scatter=None):
    data = [
        historic_scatter(x, y)
    ]
    if prediction_scatter:
        data.append(
            prediction_scatter
        )

    layout = go.Layout(
        title=title,  # Graph title
        xaxis=dict(title=x_label),  # x-axis label
        yaxis=dict(title=y_label),  # y-axis label
        hovermode='closest',  # handles multiple points landing on the same vertical
        height=600,
        showlegend=False
    )
    fig = go.Figure(data=data, layout=layout)
    return fig


def float_to_time(f):
    delta = datetime.timedelta(hours=f)
    return str(delta)


def prediction_scatter(x, y):
    scatter = go.Scatter(
        x=[x],
        y=[y],
        mode='markers',
        name='predykcja',
        marker=dict(
            size=15,
            color='rgb(255, 0, 0)'
        )
    )
    return scatter


def historic_scatter(x, y):
    scatter = go.Scatter(
        x=x,
        y=y,
        mode='markers',
        name='wyniki historyczne',
        marker=dict(
            opacity=0.8
        )
    )
    return scatter
