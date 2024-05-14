import pandas as pd
import numpy as np

path=''
X_train = pd.read_csv(path)

X_train = X_train.rename(columns={'telemetry_0': 'temp4', 
                        'telemetry_1': 'consumption',
                        'telemetry_2': 'temp1', 
                        'telemetry_3': 'ampere_add',
                        'telemetry_4': 'press_add', 
                        'telemetry_5': 'temp3',
                        'telemetry_6': 'speed', 
                        'telemetry_7': 'press1',
                        'telemetry_8': 'press2', 
                        'telemetry_9': 'temp2',
                        'telemetry_10': 'temp5', 
                        'telemetry_11': 'temp6',
                        'telemetry_12': 'item1', 
                        'telemetry_13': 'item2',
                        'telemetry_14': 'item3', 
                        'telemetry_15': 'item4',})

X_train['datetime'] = pd.to_datetime(X_train['datetime'])

X_train = X_train.fillna(X_train.iloc[:, X_train.columns.get_loc('datetime')+1:].mean())
X_train = X_train.drop(X_train[X_train.duplicated()].index)

X_train = X_train.reset_index(drop=True)