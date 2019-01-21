from mra.elements import drop_down_select_run
from mra.elements import slider_year_old
from mra.elements import slider_best10
from mra.elements import radio_sex
import dash_core_components as dcc


def test_drop_down_select_run():
    assert type(drop_down_select_run('element_id')) == dcc.Dropdown
    assert drop_down_select_run('element_id').id == 'element_id'


def test_slider_year_old():
    assert type(slider_year_old('element_id')) == dcc.Slider
    assert slider_year_old('element_id').id == 'element_id'


def test_slider_best10():
    assert type(slider_best10('element_id')) == dcc.Slider
    assert slider_year_old('element_id').id == 'element_id'


def test_radio_sex():
    assert type(radio_sex('element_id')) == dcc.RadioItems
    assert radio_sex('element_id').id == 'element_id'
