import dash_core_components as dcc
import plotly.offline as pyo
import plotly.graph_objs as go
from run_data import RunData


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


def scatter(x, y, title, x_label, y_label):
    data = [
        go.Scatter(
            x=x,
            y=y,
            mode='markers',
        )
    ]
    layout = go.Layout(
        title=title,  # Graph title
        xaxis=dict(title=x_label),  # x-axis label
        yaxis=dict(title=y_label),  # y-axis label
        hovermode='closest',  # handles multiple points landing on the same vertical
        height=800
    )
    fig = go.Figure(data=data, layout=layout)
    return fig
