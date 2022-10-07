# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import pandas as pd
import pathlib
from xlsxtemplater import to_excel, from_excel

# +
# pandas
# ... has built in read/write functions

path = pathlib.Path('test.xlsx')
df = pd.DataFrame({'col0': [0,1,2], 'col1': [1,2,3]})

df.to_excel(fpth)  
pd.read_excel(path)

# +
# xlsxtemplater
# ... allows you to write many tables to excel
# and formats the data to excel as tables for easy review 
# # ?to_excel

li = [
    {'df': df, 'sheet_name': 'mySheet'}, 
    {'df': df, 'sheet_name': 'myOtherSheet', 'notes': {'test-note':'a test dataframe note'}}, 
]
to_excel(li, 'test.xt.xlsx')
# -

from_excel('test.xt.xlsx')


