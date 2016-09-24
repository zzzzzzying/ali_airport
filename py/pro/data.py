__author__ = 'zy'


import pandas as pd
import time
start=time.time()
data1=pd.read_csv('/home/zy/testdata/4product.csv')
data2=pd.read_csv('/home/zy/testdata/5product.csv')


data=data1.merge(right=data2,how='left',on='user_id')


print data[:3]

# print data2[:3]
