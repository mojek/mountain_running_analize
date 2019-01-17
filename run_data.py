import pandas as pd
import numpy as np
from scipy import stats


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

    def load_to_dataframe(self):
        df = pd.read_csv(self.filename)
        df.dropna(subset=['best10km', 'wynik'], inplace=True)
        df = df[(np.abs(stats.zscore(df['best10km'])) < 3)]  # remove outliers
        return df
