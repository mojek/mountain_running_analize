import pytest
import numpy as np
from mra.run_data import RunData
from mra.person import Person
import pandas as pd
list_of_runs = RunData.accepted_run
first_run_key = list(list_of_runs.keys())[0]


def test_init():
    rd = RunData(first_run_key)
    assert type(rd) == RunData
    assert rd.fullname == list_of_runs[first_run_key]['fullname']
    assert rd.key == first_run_key
    assert rd.filename == list_of_runs[first_run_key]['filename']
    run_that_dont_exist = "Super run name this name dont exist"
    assert (run_that_dont_exist in list_of_runs) == False
    with pytest.raises(KeyError):
        rd = RunData(run_that_dont_exist)


def test_data_frame():
    rd = RunData(first_run_key)
    assert type(rd.dataframe) == pd.DataFrame


def test_print_predict_in_nice_string():
    assert RunData.print_predict_in_nice_string(1) == '1:00:00'
    assert RunData.print_predict_in_nice_string(1.5) == '1:30:00'
    assert len(RunData.print_predict_in_nice_string(1.521)) == 7


def test_predict():
    rd = RunData(first_run_key)
    p1 = Person(38, 1, 'W')
    prediction = rd.predict(p1)
    assert type(prediction) == float
    prediction = rd.predict(p1, True)
    assert type(prediction) == str
