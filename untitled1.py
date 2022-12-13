# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:25:29 2022

@author: Lucy
"""

import pandas as pd


years_summary = pd.read_csv('year_summary.csv')

years_summary['Percentage Increase'] = [f'{0:.2%}' if x == 0 
                                        else f'''{((years_summary.iloc[x,1] - years_summary.iloc[(x-1),1]) / 
                                              years_summary.iloc[(x-1),1]):.2%}'''
                                        for x in range(len(years_summary)) ]
                                        
years_summary.rename(columns = {"Number of Games Released": "Number of Games"}, inplace = True)                        
years_summary.to_csv('years_summary.csv')