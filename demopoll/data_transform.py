# -*- coding: utf-8 -*-

import pandas
import re

def index_data(dataframe):
    """ Indexes data set from BFS to municipalities BFS numbers contained in 
    first column values
    """
    # index dataframe using numbers in first column (BFS type, number, name)
    dataframe.index = dataframe.iloc[:,0].apply(lambda x: int(re.findall('\d+', x)[0]))
    # drop fist column
    dataframe.drop(dataframe.columns[0], axis=1, inplace=True)
    # delete index name
    del dataframe.index.name

    return dataframe.copy()

def canter_trans(terreg_set):
    # index data with BFS municipalities number
    terreg_set.index = terreg_set.iloc[:,3]
    terreg_set.sort_index(inplace=True)
    del terreg_set.index.name
    
    # select communes only
    canter_data = terreg_set[terreg_set.iloc[:,6] == 11]
    
    # turn off warning of value set on copy
    pandas.set_option('mode.chained_assignment', None)
    
    # remove duplicate
    canter_data.drop_duplicates(subset=3, inplace=True)
    
    # select canton variable only
    canter_data = canter_data.iloc[:, 2]
    
#    # convert canton values to numeric
#    canter_data = canter_data.astype('category').cat.codes
    
    return canter_data

def lanmaj_trans(lanspe_set):
    # index df with BFS municipalities numbers
    lanspe_set = index_data(lanspe_set)
    
    # create dict to code language names with nominal values
    language_codes = dict([x for x in zip(lanspe_set.columns,
                                          range(1,lanspe_set.shape[1]+1))])
    
    # convert largest language speakers count to nominal values
    language_data = lanspe_set.idxmax(axis=1).replace(language_codes)
    
    return language_data
