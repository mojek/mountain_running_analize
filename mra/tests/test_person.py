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


def test_sex_string():
    p1 = Person(38, 1, 'W')
    assert p1.sex_string() == 'Kobieta'
    p1 = Person(38, 1, 'M')
    assert p1.sex_string() == 'Mężczyzna'


def test_str():
    p1 = Person(38, 1, 'W')
    assert str(p1) == 'Kobieta, 38 lat. Czas na 10km: 1:00:00.'
    p2 = Person(37, 1.5, 'M')
    assert str(p2) == 'Mężczyzna, 37 lat. Czas na 10km: 1:30:00.'


def test_to_dataframe():
    p1 = Person(39, 1, 'M')
    assert type(p1.to_dataframe()), pd.DataFrame

    p_dic = {'K': [0], 'M': [1], 'best10km': [1], 'year_old': [38]}
    df = pd.DataFrame(data=p_dic)
    assert p1.to_dataframe()['K'].values == df['K'].values
    assert p1.to_dataframe()['M'].values == df['M'].values
    assert p1.to_dataframe()['best10km'].values == df['best10km'].values
