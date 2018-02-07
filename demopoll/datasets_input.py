#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:05:32 2018

@author: shinkoseki
"""
import sys
import pandas

# Create object containing all data sets
class DataSets:
    def __init__(self, sheet):
        for set_index in sheet.index:
            data_set = sheet.loc[set_index]
            setattr(self, data_set.set_alias, DataSet(data_set))
            
# Create data set object contining specifications   
class DataSet:
    def __init__(self, data_set):
        for set_index in data_set.index:
            setattr(self, set_index, data_set[set_index])
            
            # input data sets from csv file to data frame
            path = '%s/%s/%s/%s' % tuple([sys.path[2],
                                          'data',
                                          data_set['set_alias'],
                                          data_set['set_file']])
            if data_set['set_file'][-3:] == u'csv':
                set_data = pandas.read_csv(path,
                                           encoding='latin-1',
                                           skiprows=1)
            elif data_set['set_file'][-3:] == u'txt':
                set_data = pandas.read_csv(path,
                                           encoding='latin-1',
                                           sep='\t',
                                           header=None)
            else:
                set_data = 'No data found'
            
            self.data = set_data
            