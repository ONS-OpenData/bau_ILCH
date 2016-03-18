# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:03:35 2016

@author: Mike
"""

import pandas as pd
import sys

load_file = sys.argv[1]

obs_file = pd.read_csv(load_file, dtype = object)

# Sort out the time columns
obs_file['time_dim_item_id'] = obs_file['time_dim_item_id'].astype(str)
obs_file['time_dim_item_id'] = obs_file['time_dim_item_id'].str[0:4] + ' ' + obs_file['time_dim_item_id'].str[4:6]
obs_file['time_dim_item_id'][-1:] = ''
obs_file['time_dim_item_label_eng'] = obs_file['time_dim_item_id']

# Add a time type
obs_file['time_type'] = 'Quarter'

obs_file.to_csv('transform' + load_file[4:], index=False)

