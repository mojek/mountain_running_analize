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
        'href':
        '//stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet'

    }
]
external_scripts = [
    {
        'src': "https://www.googletagmanager.com/gtag/js?id=UA-18013743-7",
        'async': ''
    },
    '//assets/ga.js'

]


app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                external_scripts=external_scripts
                )
server = app.server
app.title = 'MRA Szczawnica'
app.layout = html.Div(className="container-fluid",
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
                                  elements.slider_year_old('select_year')]),
                          html.Div(
                              className="mycont", children=[
                                  html.Label('Najlepszy czas na 10km'),
                                  elements.slider_best10('select_best10')]),


                          html.Div([dcc.Graph(id='scatter-graph')])
                      ])


@app.callback(Output('scatter-graph', 'figure'),
              [Input('select_run', 'value'),
               Input('select_best10', 'value'),
               Input('select_year', 'value'),
               Input('select_sex', 'value')])
def update_scatter_with_prediction(selected_run,
                                   select_best10,
                                   select_year,
                                   select_sex):
    rd = RunData(selected_run)
    df = rd.dataframe
    person = Person(select_year, select_best10/100, select_sex)
    prediction = rd.predict(person)
    end_score_string = f"{RunData.print_predict_in_nice_string(prediction)}"
    title_of_scatter = f" {rd.fullname}. {person} {end_score_string}"
    scater_with_prediction = elements.prediction_scatter(
        prediction, person.best10km)

    scatter = elements.scatter(
        df['wynik'], df['best10km'],
        title_of_scatter, 'wyniki', 'najlepszy czas na 10Km',
        scater_with_prediction)
    return scatter


def run():
    app.run_server()
