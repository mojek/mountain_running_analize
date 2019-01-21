from mra.person import Person
import pytest
import pandas as pd


def test_init():
    with pytest.raises(ValueError):
        Person(38, 1, 'D')


def test_sex_dict():
    p1 = Person(38, 1, 'W')
    assert type(p1.sex_dict()) == dict
    assert p1.sex_dict() == {'K': [1], 'M': [0]}
    p2 = Person(38, 1, 'M')
    assert p2.sex_dict() == {'K': [0], 'M': [1]}


def test_to_dataframe():
    p1 = Person(39, 1, 'W')
    assert type(p1.to_dataframe()), pd.DataFrame
    p_dic = {'K': [1], 'M': [0], 'best10km': [1], 'year_old': [38]}
    df = pd.DataFrame(data=p_dic)
    print('p1', p1.to_dataframe()['K'])
    print('p2', df['K'])
    assert p1.to_dataframe()['K'].values == df['K'].values
    assert p1.to_dataframe()['best10km'].values == df['best10km'].values
