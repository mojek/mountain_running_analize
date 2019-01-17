import dash_core_components as dcc


def drop_down_select_run():
    drop_down_select_run = dcc.Dropdown(
        id='select_run',
        options=[
            {'label': 'Szczawnica - Chyża dubraszka - 19.9KM', 'value': 'chyza'},
            {'label': 'Szczawnica - Wielka Prehyba - 43.3KM', 'value': 'prehyba'}
        ],
        value='acceleration'
    )
    return drop_down_select_run
