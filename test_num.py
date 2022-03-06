[16:57] Hasuike Joe
import numpy as np
import numpy.random as rd # 解析した偏りから乱数を生成するため
from matplotlib import pyplot as plt # 解析した偏りを可視化するため
import seaborn as sns
from sympy import O; sns.set() # sns.set() ==> グラフの見た目をseabornに合わせる
# %matplotlib inline
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import selenium
import time #経過時間や処理時間記録
import collections
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.mizuhobank.co.jp/retail/takarakuji/numbers/backnumber/index.html')
# 要素の待機時間を最大10秒に設定
driver.implicitly_wait(10)
links_backnumber = driver.find_elements_by_xpath("//tr[@class=\"js-backnumber-temp-b\"]/td/a[@tabindex=\"200\"]")
links_backnumber[0].text
# '第1回〜第20回'
len(links_backnumber)
links_bn_text = []
for link in links_backnumber:
#print(link.text)
    links_bn_text.append(link.text)
winning_numbers_1000 = []
winning_numbers_100 = []
winning_numbers_10 = []
winning_numbers_1 = []
winning_numbers_all = []

for link_text in links_bn_text:
    print("before click: ", driver.current_url)
    link = driver.find_element_by_link_text(link_text)
    print(link.text)
    link.click()
    print("after click: ", driver.current_url)
    time.sleep(2)

numbers = driver.find_elements_by_xpath('//*[@id="mainCol"]/article/div/div/div[1]/table/tbody/tr/td[3]')
    for number in numbers:
        number_str = number.text
        print(number_str)
        print(int(number_str[-4]), int(number_str[-3]), int(number_str[-2]), int(number_str[-1]))
        winning_numbers_1000.append(int(number_str[-4])) # 千の位
        winning_numbers_100.append(int(number_str[-3])) # 百の位
        winning_numbers_10.append(int(number_str[-2])) # 十の位
        winning_numbers_1.append(int(number_str[-1])) # 一の位
        winning_numbers_all.append(number_str)
        winning_numbers_1000_count = collections.Counter(winning_numbers_1000)
        winning_numbers_100_count = collections.Counter(winning_numbers_100)
        winning_numbers_10_count = collections.Counter(winning_numbers_10)
        winning_numbers_1_count = collections.Counter(winning_numbers_1)
        winning_numbers_all_count = collections.Counter(winning_numbers_all)
        print("千の位：" + str(winning_numbers_1000_count.most_common()[0]))
        print("百の位：" + str(winning_numbers_100_count.most_common()[0]))
        print("十の位：" + str(winning_numbers_10_count.most_common()[0]))
        print("一の位：" + str(winning_numbers_1_count.most_common()[0]))
        print("完全一致：" + str(winning_numbers_all_count.most_common()[0]))
time.sleep(1)
driver.find_element_by_link_text("ナンバーズ 先月以前の当せん番号").click()
time.sleep(1)
# driver.close()
# driver.quit()
s = len(winning_numbers_1000), len(winning_numbers_100), len(winning_numbers_10), len(winning_numbers_1)
print(s)
driver.quit()
