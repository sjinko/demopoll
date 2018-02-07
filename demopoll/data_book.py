#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 17:11:11 2018

@author: shinkoseki
"""
import pandas

class DataBook:
    def __init__(self, book_path):
        self.book = pandas.read_excel(book_path,
                                      sheet_name=None)
    def sheet(self, sheet_name):
        #print('Printing members of the Birds class')
        return self.book[sheet_name]