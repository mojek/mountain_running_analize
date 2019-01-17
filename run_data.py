import pandas as pd
import numpy as np
from scipy import stats
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


class RunData:
    accepted_run = {
        'chyza': {
            'filename': 'data/chyza_durbaszka_all_clean_endu.csv',
            'fullname': 'Szczawnica - Chyża dubraszka - 19.9KM'
        },
        'prehyba':   {
            'filename': 'data/wielka_prehyba_all_with_endu.csv',
            'fullname': 'Szczawnica - Wielka Prehyba - 43.3KM'

        }
    }

    def __init__(self, run_name):
        founded_run = RunData.accepted_run[run_name]
        self.fullname = founded_run['fullname']
        self.filename = founded_run['filename']
        self.key = run_name
        self.dataframe = self.load_to_dataframe()
        self.linear_regresion = self.train_model_linear_regresion()

    def load_to_dataframe(self):
        def dateparse(x): return pd.datetime.strptime(x, '%Y-%m-%d')
        df = pd.read_csv(self.filename,
                         parse_dates=['race_date'],
                         date_parser=dateparse)
        df.dropna(subset=['best10km', 'wynik'], inplace=True)
        df = df[(np.abs(stats.zscore(df['best10km'])) < 3)]  # remove outliers

        df['year_old'] = df['race_date'].dt.year - df['rok_urodzenia']

        df['sex'] = df['kat_wiek']
        df['sex'] = df['sex'].apply(lambda x: x[0])
        dummy_sex = pd.get_dummies(df['sex'])
        df = pd.concat([df, dummy_sex], axis=1)

        return df

    def train_model_linear_regresion(self):
        df = self.dataframe
        X = df[['K', 'M', 'best10km', 'year_old']]
        y = df['wynik']
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.1, random_state=201)

        lm = LinearRegression()
        lm.fit(X_train, y_train)
        return lm

    def predict(self, person):
        return self.linear_regresion.predict(person)
