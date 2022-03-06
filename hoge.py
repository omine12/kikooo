#!/usr/bin/python3

from selenium import webdriver
import time
import sys, codecs

# Chromeのオプション
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Selenium Serverに接続
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
options=options)

try:
  # 要素の待機時間を最大10秒に設定
  driver.implicitly_wait(10)

  # https://pro-broccoli.com/ を開く
  driver.get('https://pro-broccoli.com/')

  # 検索ボックスに「Linux」を入力
  element_serch_box = driver.find_element_by_class_name('search_btn')
  element_serch_box.click()
  element_search_form = driver.find_element_by_class_name('searchform_input')
  element_search_form.send_keys('Linux')

  # 検索ボタンをクリック
  element_search_push = driver.find_element_by_class_name('searchsubmit')
  element_search_push.click()
  time.sleep(5)

  # 検索結果のタイトルを取得して出力
  element_titles = driver.find_elements_by_class_name("entry-title")
  for element_title in element_titles:
    if not element_title.text.strip():
      continue
    print(element_title.text.strip())

except:
  import traceback
  traceback.print_exc()

finally:
  # Chromeを終了
  time.sleep(2)
  driver.quit()

