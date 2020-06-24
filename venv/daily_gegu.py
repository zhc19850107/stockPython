import pandas as pd
import tushare as ts
from pandas import Series, DataFrame
import time

token = "b72327b6528ebe1ca9607c531be4fa94fbc18fe171e0d830823236f9"
ts.set_token(token)
pro = ts.pro_api()

# 查询当前所有正常上市交易的股票列表和近几日的交易历史数据
# data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
# s = data['ts_code'].values.tolist()
# length = len(s)  # 总长
# step = 99  # 每份的长度
# all_df = pd.DataFrame()
# for i in range(0, length, step):
#     ts_codes = ','.join(s[i: i + step])  # 逗号分隔数组元素
#     all_df = all_df.append(pro.daily(ts_code=ts_codes, start_date='20200603', end_date='20200605'), ignore_index=True)
# inner_result = pd.DataFrame()
# inner_result = pd.merge(all_df, data, how='inner', on=None, left_on='ts_code', right_on='ts_code')
# tjresult = pd.DataFrame()
# tjresult = inner_result.groupby(['industry', 'trade_date'])
# inner_result.to_csv('F:/stock_data/dayily_history' + time.strftime("%Y%m%d%H%M", time.localtime()) + '.csv',
#                     encoding='utf_8_sig')
# (tjresult.mean()).to_csv('F:/stock_data/hytj_history' + time.strftime("%Y%m%d%H%M", time.localtime()) + '.csv',
#                          encoding='utf_8_sig')

# 下载所有股票近n年的日线数据
import datetime
import time

starttime = datetime.date(2010, 1, 1)
endtime = datetime.date.today()
all_df = pd.DataFrame()
# 两个日期相差天数
days = ((endtime - starttime).days)
print('相差天数', days)
for i in range(0, days):
    # 如果遍历的500次，则停止一分钟
    if i % 500 == 0 and i != 0:
        print("暂时一分钟", i)
        time.sleep(60)
    tommorow = starttime + datetime.timedelta(days=i)
    # print(tommorow.strftime('%Y%m%d'))
    all_df = all_df.append(pro.daily(trade_date=tommorow.strftime('%Y%m%d')))
all_df.to_csv('F:/stock_data/dayily_history' + time.strftime("%Y%m%d%H%M", time.localtime()) + '.csv',encoding='utf_8_sig')
