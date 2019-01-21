import pandas as pd
import datetime


class Person:
    def __init__(self, year_old, best10km, sex):
        if sex not in ['W', 'M']:
            raise ValueError
        self.year_old = year_old
        self.best10km = best10km
        self.sex = sex

    def __str__(self):
        return f"{self.sex_string()}, {self.year_old} lat. Czas na 10km: {str(datetime.timedelta(hours=self.best10km))}."

    def sex_string(self):
        if self.sex == 'W':
            return "Kobieta"
        if self.sex == 'M':
            return "Mężczyzna"

    def sex_dict(self):
        return {'K': [int(self.sex == 'W')], 'M': [int(self.sex == 'M')]}

    def to_dataframe(self):
        best10 = {'best10km': [self.best10km]}
        year_old = {'year_old': [self.year_old]}
        sex = self.sex_dict()
        merged_dict = {**sex, **best10, **year_old}
        df = pd.DataFrame(data=merged_dict)
        return df
