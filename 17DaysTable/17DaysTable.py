#!/usr/bin/env python
# coding: utf-8

# In[31]:


"""
Automatically generate a table based on the forgetting curve.
Ref1: <Get GRE words done in 17 days>, https://book.douban.com/subject/26612036/
Ref2: https://en.wikipedia.org/wiki/Forgetting_curve
"""

import numpy as np
import pandas as pd
import math

page_total = int(input(prompt='Total pages (default=550): ') or '550')
page_perlist = int(input(prompt='Pages per list (default=50): ') or '50')
file_export = '~/days_table.csv'
days_periodic = [0, 1, 2, 4, 7, 15]

# Define the length and name of rows and columns.
lists_length = math.ceil(page_total / page_perlist)
days_length = lists_length + sum(days_periodic)
columns_shortname = list('L'+str(_) for _ in range(1,lists_length+1))
columns_longname = list(str(_)+'-'+str(_+50)  for _ in range(1,page_total,page_perlist))
rows_name = range(1, days_length+1)

# Create a blank table with the specific length of rows and columns.
days_table = pd.DataFrame(np.zeros((days_length, lists_length), dtype=int), 
                          columns=[columns_shortname, columns_longname], index=rows_name)
days_table.index.name = 'Days'
days_table.columns.names = ['Lists', 'Pages']
days_table[days_table == 0] = ''

# Fill with periodic days 
for i in range(lists_length):
    days_index = list(np.cumsum(days_periodic) + range(days_length)[i] + 1)
    days_table.loc[days_index, columns_shortname[i]] = str(columns_shortname[i])
    days_table.loc[days_index[0], columns_shortname[i]] =  '* + '.join([columns_shortname[i]] * 2)
    days_table.loc[days_index[1:-2:2], columns_shortname[i]] = str(columns_shortname[i]) + '(r)'

days_table.to_csv(file_export)

days_table

