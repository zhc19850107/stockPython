from selenium import webdriver  # 从selenium导入webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://quote.eastmoney.com/f1.html?code=000988&market=2')  # 东方财富分时交易数据
# firstdivcontent = driver.find_element_by_id("listTable1").text
# print('first',firstdivcontent)

# 获取当前页数
pagecount = (driver.find_element_by_class_name('count').text);
try:
    for i in range(0, int(pagecount)):
        input = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/div[2]/ul/li[6]/div/input")
        input.clear()
        input.send_keys(str(i + 1))  # i为循环的数字
        # 点击go键
        gobutton = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/div[2]/ul/li[6]/button")
        gobutton.click()
        time.sleep(5)
        WebDriverWait(driver, 30,0.5).until(EC.presence_of_element_located((By.ID,"listTable1")))
        for j in range(1, 5):
            for k in range(1, 37):
                tradetime_str = "/ html / body / div[1] / div[2] / div[4] / div[1] / div[" + str(
                    j) + "] / table / tbody / " + "tr[" + str(k) + "]/td[1]"
                # print(tradetime_str)
                tradetime = driver.find_element_by_xpath(tradetime_str).text
                # 共计四个div
                # / html / body / div[1] / div[2] / div[4] / div[1] / div[1] / table / tbody / tr[1] / td[1]
                # / html / body / div[1] / div[2] / div[4] / div[1] / div[1] / table / tbody / tr[2] / td[1]
                # / html / body / div[1] / div[2] / div[4] / div[1] / div[1] / table / tbody / tr[1] / td[2]
                # / html / body / div[1] / div[2] / div[4] / div[1] / div[2] / table / tbody / tr[1] / td[1]
                tradeprice_str = "/ html / body / div[1] / div[2] / div[4] / div[1] /  div[" + str(
                    j) + "]  / table / tbody / " + "tr[" + str(k) + "]/td[2]"
                tradeprice = driver.find_element_by_xpath(tradeprice_str).text
                tradecount_str = "/ html / body / div[1] / div[2] / div[4] / div[1] /  div[" + str(
                    j) + "]  / table / tbody / " + "tr[" + str(k) + "]/td[3]"
                tradecount = driver.find_element_by_xpath(tradecount_str).text
                # print(j,k,tradetime, tradeprice, tradecount)
        # time.sleep(5)
    print(i)
    driver.quit()
# 退出驱动程序
except Exception as e:
    print("Exception found",format(e))
    driver.quit()
