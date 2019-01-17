import pytest
from run_data import RunData


class TestRunData(object):
    def test_init(self):
        list_of_runs = RunData.accepted_run
        rd = RunData(list_of_runs[0])
        assert type(rd) == RunData
        assert rd.run_name == list_of_runs[0]
        run_that_dont_exist = "Super run name this name dont exist"
        assert (run_that_dont_exist in list_of_runs) == False
        with pytest.raises(ValueError):
            rd = RunData(run_that_dont_exist)
