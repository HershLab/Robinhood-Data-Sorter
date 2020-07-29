import pandas as pd
import os
import numpy as np
import xlsxwriter



all_df_list = []

cwd = os.path.abspath('')
files = os.listdir(cwd)
writer = pd.ExcelWriter(cwd + '//Sorted_Stocks.xlsx', engine = 'xlsxwriter')
counter = 0

for file in files:
    if file.endswith ('.csv'):
        all_df_list.append(pd.read_csv(file))
        if(len(all_df_list) > 50):
            counter = counter + 1
            appended_df = pd.concat(all_df_list)
            appended_df.to_excel(writer, sheet_name = 'Set' + str(counter))
            all_df_list = []

writer.save()
writer.close()

#appended_df.to_excel("Sorted_Stocks.xlsx", index=False)
