#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:57:32 2018

@author: shinkoseki
"""
#%%
# load python 2.7 distribution modules
import rpy2
import pandas as pd
import sys

#%%
# load demopoll modules
from demopoll import *

#%%
def main():

# 1. Import data book
    # set path to data book excel file
    book_path = sys.path[2]+'/data/databook.xlsx'
    # load data book as dictionary of data frames
    book = DataBook(book_path)
    # load dataset sheet as data frame
    datasets_sheet = book.sheet('datasets')
    # load data sheet as data frame
    data_sheet = book.sheet('data')
    # load variables sheet as data frame
    variables_sheet = book.sheet('variables')
    
# 2. Import data sets
    datasets = DataSets(datasets_sheet)

# 3. Transform data sets to usable data
    # list which data set needs to be modfied
    for i in data_sheet.index:
        if data_sheet.loc[i, 'data_alias'][:-5] != data_sheet.loc[i, 'data_set'][:-4]:
            print data_sheet.loc[i, 'data_alias'][:-5]
    
    
    # create cantonal territory covariate
    canter_data = data_transform.canter_trans(datasets.terreg_set.data)
    
    # create language majority covariate
    lanmaj_data = data_transform.lanmaj_trans(datasets.lanspe_set.data)
    
    # create distance network covariate
    ## MISSING DATA
    
    # create denomination majority covariate
    
    
    



# 4. Compute variables from data


# 5. Build RSiena Model


# 4. Output variables

    
if __name__=='__main__':
    main()