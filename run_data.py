import pandas as pd


class RunData:
    accepted_run = ['chyza', 'prehyba']
    file_names = ['data/chyza_durbaszka_all_clean_endu.csv',
                  'data/wielka_prehyba_all_with_endu.csv']

    def __init__(self, run_name):
        if run_name not in RunData.accepted_run:
            raise ValueError
        self.run_name = run_name
