import pytest
from mra.run_data import RunData
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
