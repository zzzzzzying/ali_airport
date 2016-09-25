#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-24 21:52:15
# @Author  : chensijia (2350543676@qq.com)
# @Version : 0.0.0
# @Style   : Python3.4
#
# @Description: 

## import python`s own lib
import os


## import third party lib
import pandas as pd

## import local lib


def t_v(x):
    t_t = x.strip().split("-")
    tt_fomat = t_t[0] + "-" + t_t[1] + "-" + t_t[2] + " " + \
                t_t[3] + ":" + t_t[4] + ":" + t_t[5]
    return tt_fomat


# ZH9615
# HO1078
def flight_destination_id(flight_id):
    # the last number is odd
    if int(flight_id[-2:]) % 2 == 0:
        return int(flight_id[2])
    else:
        return int(flight_id[3])
    return int(flight_id[3])


if __name__ == '__main__':
    t_str = "2016-09-10-20-35-01"
    print(t_v(t_str))

    print(flight_destination_id("ZH9615"))
    print(flight_destination_id("HO1078"))