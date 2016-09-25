#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-24 17:54:55
# @Author  : chensijia (2350543676@qq.com)
# @Version : 0.0.0
# @Style   : Python3.4
#
# @Description: 

## import python`s own lib
import os
from datetime import datetime

## import third party lib
import pandas as pd

## import local lib
from my_tools import t_v

Competition_HOME = "/home/csjx/languageCode/DeveloperArea/DM_competition/ali_airport"
Data_HOME = os.path.join(Competition_HOME, "mine_data")
Code_HOME = os.path.join(Competition_HOME, "mine_code")
Info_HOME = os.path.join(Competition_HOME, "mine_info")

# print(Competition_HOME)

## for season one, loading original data
# sheet1: airport_gt_WiFi_ap
S1_ORDa_ap_path = os.path.join(Data_HOME, "S1_OR_Data", "airport_gz_WiFi_ap.csv")
# sheet2: airport_gt_security_check
S1_ORDa_sc_path = os.path.join(Data_HOME, "S1_OR_Data", "airport_gz_security_check.csv")
# sheet3: airport_gt_departure
S1_ORDa_dt_path = os.path.join(Data_HOME, "S1_OR_Data", "airport_gz_departure.csv")

# all the data readed as DataFrame
S1_OR_ap_df = pd.read_csv(S1_ORDa_ap_path, skip_blank_lines = False, index_col = False,
                            parse_dates = ["time_stamp"], 
                            date_parser = lambda x: t_v(x))

S1_OR_sc_df = pd.read_csv(S1_ORDa_sc_path, skip_blank_lines = False, index_col = False,
                            parse_dates = ["security_time"])

S1_OR_dt_df = pd.read_csv(S1_ORDa_dt_path, skip_blank_lines = False, index_col = False,
                            parse_dates = ["flight_time", "checkin_time"])





if __name__ == '__main__':
    print(S1_OR_ap_df)
    print(S1_OR_sc_df)
    print(S1_OR_dt_df)