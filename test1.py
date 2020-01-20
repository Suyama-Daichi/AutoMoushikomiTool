# PythonでSeleniumのwebdriverモジュールをインポート
from selenium import webdriver
# Selectタグを操作できるモジュール
from selenium.webdriver.support.ui import Select
import time

# 申し込みたい公演の申し込みURL
koenUrl = "https://www.fc-member.johnnys-net.jp/performance/applicant/id/562"

# 公演No(ここに申し込みたい公演の番号を設定)
koenNos = [
    "04101T", 
    "04111T", 
    "04112T", 
    "04151T", 
    "04161T",
    "04162T",
    "04171T",
    "04172T",
    "04181T",
    "04182T",
    "04191T",
    ]
# 枚数
maisu = 2
# いつでもよいを選択するか(Trueならいつでもよい)
itsudemoOK = True








# 1.操作するブラウザを開く
driver = webdriver.Chrome('chromedriver.exe')

# 2.操作するページを開く
driver.get('https://www.fc-member.johnnys-net.jp/login/index/f/JI')

# ログインIDを入力する
driver.find_element_by_id("member_id").send_keys("00886551")

# パスワードを入力する
driver.find_element_by_id("password").send_keys("luna1213")

# ログインボタンをクリックする
driver.find_element_by_xpath("//*/section/form/div[2]/div/button").click()

for koenNo in koenNos:
    # 指定の公演の申し込みページを開く
    driver.get(koenUrl)

    # チェックボックスにチェックを入れる
    driver.find_element_by_class_name("checkbox").click()

    # 申し込み本ページに遷移する
    driver.find_element_by_id("applicant-link").click()

    # 第一希望を選択する
    Select(driver.find_element_by_id("request1")).select_by_value(koenNo)

    # 第四希望を選択する()
    Select(driver.find_element_by_id("request4")).select_by_index(1 if itsudemoOK else 2)

    # 次へボタンをクリック
    driver.find_element_by_xpath("//*/section/form/div[2]/div/button").click()

    # チケット枚数を選択
    Select(driver.find_element_by_id("qty")).select_by_index(maisu)

    # 次へボタンをクリック
    driver.find_element_by_xpath(
        "//*/section/form/div[2]/div[1]/button").click()

    time.sleep(2)

    # 申し込むボタンをクリック
    driver.find_element_by_xpath(
        "//*/section/form/div[2]/div[1]/button").click()

    time.sleep(2)
else:
    print("申し込み完了！")
