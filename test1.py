# PythonでSeleniumのwebdriverモジュールをインポート
from selenium import webdriver
# Selectタグを操作できるモジュール
from selenium.webdriver.support.ui import Select

import time

# 1.操作するブラウザを開く
# /Users/Kenta/Desktop/Selenium/chromedriver
driver = webdriver.Chrome('chromedriver.exe')

# 2.操作するページを開く
driver.get('https://www.fc-member.johnnys-net.jp/login/index/f/JI')

# 基本設定はここまで。↑は使い回し可能。ここから下は、やりたい動作によって増える

# ログインIDを入力する
driver.find_element_by_id("member_id").send_keys("00886551")

# パスワードを入力する
driver.find_element_by_id("password").send_keys("luna1213")

# ログインボタンをクリックする
driver.find_element_by_xpath("//*/section/form/div[2]/div/button").click()

# 指定の公演の申し込みページを開く
driver.get("https://www.fc-member.johnnys-net.jp/performance/applicant/id/565")

# チェックボックスにチェックを入れる
driver.find_element_by_class_name("checkbox").click()

# 申し込み本ページに遷移する
driver.find_element_by_id("applicant-link").click()

# 第一希望を選択する
Select(driver.find_element_by_id("request1")).select_by_value("05312J")

# 第四希望を選択する()
Select(driver.find_element_by_id("request4")).select_by_index(2)

# 次へボタンをクリック
driver.find_element_by_xpath("//*/section/form/div[2]/div/button").click()

# チケット枚数を選択
Select(driver.find_element_by_id("qty")).select_by_index(2)

# 次へボタンをクリック
driver.find_element_by_xpath("//*/section/form/div[2]/div[1]/button").click()

# 申し込むボタンをクリック
driver.find_element_by_xpath("//*/section/form/div[2]/div[1]/button").click()