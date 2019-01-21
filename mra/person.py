import pandas as pd


class Person:
    def __init__(self, year_old, best10km, sex):
        if sex not in ['W', 'M']:
            raise ValueError
        self.year_old = year_old
        self.best10km = best10km
        self.sex = sex

    def sex_dict(self):
        return {'K': [int(self.sex == 'W')], 'M': [int(self.sex == 'M')]}

    def to_dataframe(self):
        best10 = {'best10km': [self.best10km]}
        year_old = {'year_old': [self.year_old]}
        sex = self.sex_dict()
        merged_dict = {**sex, **best10, **year_old}
        df = pd.DataFrame(data=merged_dict)
        print(df)
        return df
