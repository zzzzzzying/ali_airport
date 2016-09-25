#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-24 21:57:19
# @Author  : chensijia (2350543676@qq.com)
# @Version : 0.0.0
# @Style   : Python3.4
#
# @Description: 

## import python`s own lib
import os
import sys
sys.path.insert(0, "../")

## import third party lib
import pandas as pd

## import local lib
from BASIC_INFO import *
from my_tools import flight_destination_id

class ProProcess_Sheets(object):
    def __init__(self, sheet_df):
        self._sheet_df = sheet_df

    def extract_ap_tag(self):
        self._sheet_df["ap_floor"] = self._sheet_df["WiFi_ap_tag"].apply(lambda x: x[:4])
        
        self._sheet_df["ap_floor_district"] = \
                    self._sheet_df["WiFi_ap_tag"].apply(lambda x: x[4:7])
        # print(self._sheet_df)
    # def time_proprcess(self):
    #     self._sheet_df["time_stamp_minute"] = \
    #                 self._sheet_df["time_stamp"].apply(lambda x: x)

    ## get the destination from flight_ID
    # ZH9615
    def get_flight_destination_and_company(self):
        self._sheet_df["flight_company_ID"] = \
                    self._sheet_df["flight_ID"].apply(lambda x: x[:2])
        self._sheet_df["flight_destination_ID"] = \
                    self._sheet_df["flight_ID"].apply(lambda x: flight_destination_id(x))
    def get_flight_num_passenger(self, ):


if __name__ == '__main__':
    pp_s = ProProcess_Sheets(S1_OR_ap_df)
    pp_s.extract_ap_tag()