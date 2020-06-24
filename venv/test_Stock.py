import tushare as ts

tooken = 'b72327b6528ebe1ca9607c531be4fa94fbc18fe171e0d830823236f9'
ts.set_token(tooken)

# data = ts.get_hist_data('000988', ktype='5', start='2020-01-01', end='2020-01-14')
# print(data)

# pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple gevent
# https://blog.csdn.net/xqnode/article/details/88431139 升级pip
# https://www.cnblogs.com/laolv/p/9165066.html 升级lxml
# print(ts.get_today_all())

# df = ts.get_tick_data('000988', date='2020-01-13')
# history = ts.get_hist_data('000988', start='2020-01-16', end='2020-01-18', ktype=5)
# print(history)

# hg = ts.get_sina_dd('000988', date='2020-03-17', vol=200)  ##获取大单交易数据
# 取得某个元素
# print(hg.at[1, 'price'])

# 遍历所有行
# for index in hg['price'].index:
#     v_price = hg['price'].get(index)
    # print(v_price)

# 获取所有行
# for index, row in hg.iterrows():
#     print(row["price"],row["volume"],row["preprice"])

# hg.to_excel('D:/huagong.xlsx')

# dz = ts.get_sina_dd('002008', date='2020-03-13', vol=200)  ##获取大单交易数据
# dz.to_excel('D:/dazu.xlsx')

# xq = ts.get_sina_dd('002291', date='2020-03-13', vol=200)  ##获取大单交易数据
# xq.to_excel('D:/xql.xlsx')

# pro = ts.pro_api()
# jiaoyi = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
# print(jiaoyi)


# pro = ts.pro_api()
# df = pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province,main_business')
# print(df)

# 获取股票的分笔交易数据
# fbjy = ts.get_today_ticks('000988')
# print(fbjy)

v_fbjy = ts.get_hist_data('000988', ktype='5')
# v_fbjy.to_excel('D:/dazu_five_minutes.xlsx')
# for index,row in v_fbjy.iterrows():
#     print(row["open"],row["high"],row["close"])
    # print((row["date"])) TODO 日期型数据未调试通，在打印是报错keyerror

df = ts.get_tick_data('000988',date='2020-03-16',src='tt')
# print(df.head(10))


# 获取每日收盘的行情数据
# print(ts.get_day_all())




# print(ts.get_realtime_quotes('000988'))

pro = ts.pro_api()
lsjy = pro.daily(ts_code='', start_date='20200210', end_date='20200318')
# lsjy.to_excel('D:/lsjy.xlsx')

print(ts.pro_bar(ts_code='000988.SZ', adj='qfq', start_date='20180101', end_date='20181011',freq='W'))

