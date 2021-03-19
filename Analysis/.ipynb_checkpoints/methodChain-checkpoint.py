import os
import pandas as pd
import numpy as np

# Method Chaining
def load_and_processText(path):
    # Chain 1: Data loaded and missing data removed
    df1 = (
        pd.read_csv(os.path.join('..','Dataset','helpfulness_reviews_worst_apps.csv'))
            .dropna()
            .loc[lambda x: x['text'] != '']
            # Removing no text entries
            .reset_index(drop=True)
    )
    # Chain 2: Drop irrelevant columns
    df2 = (
        # Currently just dropping the following:
        # appTitle, userName, date, score
        df1.drop(['appTitle', 'userName', 'date', 'score'], axis=1)
            .reset_index(drop=True)
    )
    return df2

def load_and_processSlang(path):
    # Chain 1: Data loaded
    df1 = (
        pd.read_csv(os.path.join('..','Dataset','slangs.csv'))
    )
    return df1

