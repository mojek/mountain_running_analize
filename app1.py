import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import elements
from run_data import RunData
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]


app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets
                )
server = app.server
app.title = 'Mountain running analizer'
app.layout = html.Div(className="container-fluid",
                      children=[
                          html.H1(children='Mountain running analizer'),

                          html.Div(
                              className="mycont2", children=[
                                  html.Label('Wiek biegacza'),
                                  elements.slider_year_old('select_year_old')]),
                          html.Div(
                              className="mycont", children=[
                                  html.Label('Najlepszy czas na 10km'),
                                  elements.slider_best10('select_best10')]),
                          html.Div(
                              [elements.drop_down_select_run('select_run')]),

                          html.Div([dcc.Graph(id='scatter-graph')])
                      ])


@app.callback(Output('scatter-graph', 'figure'),
              [Input('select_run', 'value')])
def update_scatter(selected_run):
    rd = RunData(selected_run)
    df = rd.dataframe
    scatter = elements.scatter(
        df['wynik'], df['best10km'],
        rd.fullname, 'wyniki', 'rok_urodzenia', True)
    return scatter


if __name__ == '__main__':
    app.run_server()
