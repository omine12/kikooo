#!/usr/bin/python3

from selenium import webdriver
import time    #経過時間や処理時間記録
import pandas as pd    #データ解析を支援。ExcelやCSV
from webdriver_manager.chrome import ChromeDriverManager

USER = "test_user"
PASS = "test_pw"

#GoogleChromeを起動
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(3)
#ログインするサイトへアクセス
url_login = "https://kino-code.work/membership-login/"
browser.get(url_login)
time.sleep(3)
print("ログインページにアクセスしました")

# ユーザ名を入力
element = browser.find_element_by_id("swpm_user_name")  #HTMLの要素を指定
element.clear()  #値をクリアにする。テキストボックス内の文字を消す。
element.send_keys(USER)  #テキストボックスに入力。変数USERを指定。
element = browser.find_element_by_id("swpm_password")
element.clear()
element.send_keys(PASS)
print("フォーム送信")

#入力したデータをクリック
browser_from = browser.find_element_by_name("swpm-login") #nameを指定して要素を取得
time.sleep(3)
browser_from.click()#クリックする
print("情報を入力してログインボタンを押しました")

#ウェブサイトへアクセス
url = "https://kino-code.work/member-only/"
time.sleep(3)
browser.get(url)
print(url, "アクセス完了")

#ダウンロードボタンをクリック
frm = browser.find_element_by_xpath("/html/body/div/div[3]/div/main/article/div/p[2]/button") #
time.sleep(1)
frm.click()
print("ダウンロードボタンをクリック")

#browser = webdriver.Chrome()   #Mac
#browser.implicitly_wait(3)   #Chromeドライバが見つかるまでの待ち時間。3秒間待つ


