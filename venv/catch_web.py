import requests
payload = {'key1': 'value1', 'key2': 'value2'}
ret = requests.get("http://stockhtm.finance.qq.com/sstock/quotpage/q/000988.htm#detail")
print(ret.text)
