import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from mra import elements
from mra.run_data import RunData
from mra.person import Person

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]
external_scripts = [
    {
        'src': "https://www.googletagmanager.com/gtag/js?id=UA-18013743-7",
        'async': ''
    },
    '//assets/ga.js'

]


app_dash = dash.Dash(__name__,
                     external_stylesheets=external_stylesheets,
                     external_scripts=external_scripts
                     )
server = app_dash.server
app_dash.title = 'MRA Szczawnica'
app_dash.layout = html.Div(className="container-fluid",
                           children=[
                               html.H1(children='MRA Szczawnica'),
                               html.Div(
                                   [elements.drop_down_select_run('select_run')]),
                               html.Div(
                                   className="mycont3", children=[
                                       html.Label('Płeć biegacza'),
                                       elements.radio_sex('select_sex')]),
                               html.Div(
                                   className="mycont2", children=[
                                       html.Label('Wiek biegacza'),
                                       elements.slider_year_old('select_year_old')]),
                               html.Div(
                                   className="mycont", children=[
                                       html.Label('Najlepszy czas na 10km'),
                                       elements.slider_best10('select_best10')]),


                               html.Div([dcc.Graph(id='scatter-graph')])
                           ])


@app_dash.callback(Output('scatter-graph', 'figure'),
                   [Input('select_run', 'value'),
                    Input('select_best10', 'value'),
                    Input('select_year_old', 'value'),
                    Input('select_sex', 'value')])
def update_scatter_with_prediction(selected_run, select_best10, select_year_old, select_sex):
    rd = RunData(selected_run)
    df = rd.dataframe
    person = Person(select_year_old, select_best10/100, select_sex)
    prediction = rd.predict(person)
    title_of_scatter = f" {rd.fullname}. {person} Przewidywany wynik końcowy: {RunData.print_predict_in_nice_string(prediction)}"
    scater_with_prediction = elements.prediction_scatter(
        prediction, person.best10km)
    scatter = elements.scatter(
        df['wynik'], df['best10km'],
        title_of_scatter, 'wyniki', 'najlepszy czas na 10Km', scater_with_prediction)
    return scatter


def run():
    app_dash.run_server()
