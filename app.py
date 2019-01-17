import dash
import dash_core_components as dcc
import dash_html_components as html
import elements
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
                external_stylesheets=external_stylesheets)

app.layout = html.Div(className="container-fluid",
                      children=[
                          html.H1(children='Mountain running analizer'),
                          html.Div([elements.drop_down_select_run()])
                      ])


if __name__ == '__main__':
    app.run_server()
