# PythonでSeleniumのwebdriverモジュールをインポート
from selenium import webdriver
# Selectタグを操作できるモジュール
from selenium.webdriver.support.ui import Select
import time

# 公演No(ここに申し込みたい公演の番号を設定)
koenNos = ["04101T","04111T","04112T"]
# 枚数
maisu = 2

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

for koenNo in koenNos:
    # 指定の公演の申し込みページを開く
    driver.get("https://www.fc-member.johnnys-net.jp/performance/applicant/id/562")

    # チェックボックスにチェックを入れる
    driver.find_element_by_class_name("checkbox").click()

    # 申し込み本ページに遷移する
    driver.find_element_by_id("applicant-link").click()

    # 第一希望を選択する
    Select(driver.find_element_by_id("request1")).select_by_value(koenNo)

    # 第四希望を選択する()
    Select(driver.find_element_by_id("request4")).select_by_index(2)

    # 次へボタンをクリック
    driver.find_element_by_xpath("//*/section/form/div[2]/div/button").click()

    # チケット枚数を選択
    Select(driver.find_element_by_id("qty")).select_by_index(maisu)

    # 次へボタンをクリック
    driver.find_element_by_xpath("//*/section/form/div[2]/div[1]/button").click()

    time.sleep(2)

    # 申し込むボタンをクリック
    driver.find_element_by_xpath("//*/section/form/div[2]/div[1]/button").click()

    time.sleep(2)
else:
    print("申し込み完了！")