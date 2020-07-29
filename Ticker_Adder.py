import pandas as pd
import os

cwd = os.path.abspath('')
files = os.listdir(cwd)


for file in files:
    if file.endswith ('.csv'):
        df_file = pd.read_csv(file)
        newFileName = file
        newFileName = newFileName.replace('.csv', ' ')
        df_file.insert(0, 'Ticker', newFileName)
        df_file.to_csv(file, index=False)