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

    ## Area to solve sheet a
    def extract_ap_tag(self):
        self._sheet_df["ap_floor"] = self._sheet_df["WiFi_ap_tag"].apply(lambda x: x[:4])
        
        self._sheet_df["ap_floor_district"] = \
                    self._sheet_df["WiFi_ap_tag"].apply(lambda x: x[4:7])
        # print(self._sheet_df)
    def time_proprcess(self, time_col_name):
        self._sheet_df[time_col_name + "_date"] = self._sheet_df[time_col_name].\
                                                    apply(lambda x: x.date())
        self._sheet_df[time_col_name + "_hour"] = self._sheet_df[time_col_name].\
                                            apply(lambda x: x.hour)
        self._sheet_df[time_col_name + "_minute"] = self._sheet_df[time_col_name].\
                                                    apply(lambda x: x.minute)
        self._sheet_df[time_col_name + "_second"] = self._sheet_df[time_col_name].\
                                                    apply(lambda x: x.second)
        self._sheet_df[time_col_name + "_dayofweek"] = self._sheet_df[time_col_name].\
                                                    apply(lambda x: x.dayofweek)
        self._sheet_df[time_col_name + "_weekdayname"] = self._sheet_df[time_col_name].\
                                                    apply(lambda x: x.weekday_name)

        # print(self._sheet_df)


    ## Area to solve sheet b & c
    ## get the destination from flight_ID
    # ZH9615
    def get_flight_destination_and_company(self):
        self._sheet_df["flight_company_ID"] = \
                    self._sheet_df["flight_ID"].apply(lambda x: x[:2])
        self._sheet_df["flight_destination_ID"] = \
                    self._sheet_df["flight_ID"].apply(lambda x: flight_destination_id(x))
        print(self._sheet_df)
    
    # add flight time for this sheet
    def 
    def insert_flight_departure_time(self, departure_sheet_df):
        flight_dt_df = departure_sheet_df[["flight_ID", "flight_time"]]
        print(flight_dt_df)
        # flight_dt_map = flight_dt_df.groupby(by = ["flight_ID"])["flight_time"].apply(lambda x: x.tolist()).\
        #                         to_dict()
        flight_dt_map = flight_dt_df.groupby(by = ["flight_ID"])["flight_time"].apply(lambda x: print(x))
        print(flight_dt_map)
        #flight_departure_map = flight_departure


if __name__ == '__main__':
    ## here to solve sheet a: 
    pp_s = ProProcess_Sheets(S1_OR_ap_df)
    pp_s.extract_ap_tag()
    pp_s.time_proprcess(time_col_name = "time_stamp")

    ## here to solve sheet b & c: 
    pp_s = ProProcess_Sheets(S1_OR_sc_df)
    pp_s.time_proprcess("security_time")
    pp_s.get_flight_destination_and_company()
