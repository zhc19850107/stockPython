import tushare as ts
import pandas as pd
from pandas import Series, DataFrame
import time
import numpy as np
import matplotlib.pyplot as plt

tooken = 'b72327b6528ebe1ca9607c531be4fa94fbc18fe171e0d830823236f9'
ts.set_token(tooken)

pro = ts.pro_api()
# 某个时间段所有行情信息
# lsjy = pro.daily(ts_code='', start_date='20200210', end_date='20200318')

# lshq_all是一个pandas.core.frame.DataFrame类型的数据
# lshq_all = pro.daily(trade_date='20200319')

# 找出某天涨停板的股票
# for index, row in lshq_all.iterrows():
#     if row['pct_chg'] > 9:
#         print(row['pct_chg'])

# 找出某只股票指定时间段，最高价和最低价和变化情况
# lshq_hg = pro.daily(ts_code='000988.SZ', start_date='20200101', end_date='20200322')
# lshq_hg.to_excel('D:/lshq_hg.xlsx')

# currentdate = time.strftime("%Y%m%d", time.localtime())
# lshq_hg = pro.daily(ts_code='000988.SZ', start_date='20200101', end_date=currentdate)

# 常用的聚合函数
# print(lshq_hg['high'].size)
# print(lshq_hg['high'].sum())
# print(lshq_hg['high'].mean())
# print(lshq_hg['high'].count())
# print(lshq_hg['high'].max())
# print(lshq_hg['high'].min())
# 各列的数据类型
# print(lshq_hg.dtypes)
# print(lshq_hg.ndim)
# 横坐标签名
# print(lshq_hg.axes)

# dataframe的切片函数应用
# print(lshq_hg.iloc[2,:])#输出第二行所有列
# print(lshq_hg.iloc[0,[0,2]])#第0行，第0列和第2列
# print(lshq_hg['open'].iloc[2])#第几行，某列的值

########################按照某列或者某几列进行去重###########
# subset：可以指定传入单个列标签或者一个列标签的列表，默认是使用所有的列标签，即会删除一整行
# keep：有{‘first’, ‘last’, False}三个可供选择, default ‘first’，意味着除了第一个后面重复的全部删除
# # inplace:返回是否替代过的值，默认False,即不改变原数据。
# # df=lshq_hg.drop_duplicates(subset=['ts_code','open'],keep='first')
# print(df)

# 去除有NaN值的行或列(axis=0去除行，=1去除列)
# df_row_nan = lshq_hg.dropna(axis=0)
# df_col_nan = lshq_hg.dropna(axis=1)

# 去除某列或者某几列
# df_del_col = lshq_hg.drop(['ts_code','trade_date'],axis=1)
# print(df_del_col)

# 去除还有某个数的行
# row_list = lshq_hg[lshq_hg['trade_date'] == '20200217'].index.tolist() # 获得含有该值的行的行号
# df_del_row = lshq_hg.drop(row_list)
# print(df_del_row)

# 用已有的列进行运算创建新的列
# lshq_hg['jiacha'] = lshq_hg['high']-lshq_hg['low']

# 修改列名（只需写上需要修改的列）inplace=True表示修改lshq_hg，若为False表示只返回一个修改后的数据
# lshq_hg.rename(columns={'jiacha':'最高最低'},inplace = True)
# print(lshq_hg)

# 修改数据
# lshq_hg.iloc[1,2] = 10

# 两个dataframe合并在一起，axis表示连接的方向，axis=0表示两个dataframe的行数会增加，axis=1，表示会加上新的列
# 一：如果列名相同则直接共用列 #连接后行数是以前的2倍，列数不变
# lshq_hg=pd.concat([lshq_hg,lshq_hg],axis=0)

# 二： 如果列名不同会生成新的列

# 输出为excel或者csv格式,csv文件里的数据被读取时数据类型默认为object，excel则会保留原有的数据类型
# lshq_hg.to_excel('D:/lshq_hg' + time.strftime("%Y%m%d%H%M", time.localtime()) + '.xlsx')
# lshq_hg.to_csv('F:/stock_data/lshq_hg' + time.strftime("%Y%m%d%H%M", time.localtime()) + '.csv')

# 获取日线数据
# df = pro.daily(trade_date='20180810')

# df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
# df.plot.pie(subplots=True)

# s = Series( np. random. randn( 10). cumsum(), index= np. arange( 0, 100, 10))
# s. plot()
# plt.show()

# 获取所有所有股票代码信息，然后遍历所有的历史数据
# 一：下载所有股票代码列表
data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
dayily_history = pd.DataFrame()
count = 0

ts_code_v = ''
for row in data.itertuples():
    ts_code_v = getattr(row, 'ts_code')



# for row in data.itertuples():
#     ts_code_v = getattr(row, 'ts_code')
#     name = getattr(row, 'name')
#     count= count +1
#     if count% 500 == 0:
#         print("Start : %s" % time.ctime())
#         time.sleep(60)
#         print("End : %s" % time.ctime())
#         break
# dayily_history.append(pro.daily(ts_code=ts_code_v, start_date='20200608', end_date='20200608'))
# dayily_history['股票名称'] = name
# print(dayily_history)
# dayily_history.to_csv('F:/stock_data/dayily_history' + time.strftime("%Y%m%d%H%M", time.localtime()) + '.csv')
# print(1530%500)
# ts_code_v =['000988.SZ','000978.SZ']
# print(pro.daily(ts_code='000988.SZ,000978.SZ', start_date='20200608', end_date='20200608'))

