# PythonでSeleniumのwebdriverモジュールをインポート
from selenium import webdriver
# Selectタグを操作できるモジュール
from selenium.webdriver.support.ui import Select
import time

# 当落を確認したい公演の申し込み確認URL
koenUrl = "https://www.fc-member.johnnys-net.jp/performance/status/id/559"

# ログインしたいユーザーの会員番号を設定
memberIds = [
    "00886551",
    # "00886549",
    ]
# 今は同一パスワードのみ対応
password = ["luna1213"]

# 落選整理番号
rakusenList = []
# 当選整理番号
tousenList = []

# 操作するブラウザを開く
driver = webdriver.Chrome('chromedriver.exe')

for memberId in memberIds:
    # ログインページを開く
    driver.get('https://www.fc-member.johnnys-net.jp/login/index/f/JI')

    # ログインIDを入力する
    driver.find_element_by_id("member_id").send_keys(memberId)

    # パスワードを入力する
    driver.find_element_by_id("password").send_keys(password[0])

    # ログインボタンをクリックする
    driver.find_element_by_xpath("//*/section/form/div[2]/div/button").click()

    # 指定の公演の申し込みページを開く
    driver.get(koenUrl)

    for index, target in enumerate(driver.find_elements_by_class_name("round-button")):
        driver.find_element_by_xpath(F"//*/section[2]/div[{index + 1}]/div[2]/a").click()
        seiribango = driver.find_element_by_css_selector("#main > section:nth-child(4) > div > div.block-title > h4").text
        for result in driver.find_elements_by_class_name("tourText"):
            if "落選" in result.text:
                rakusenList.append(seiribango)
            else:
                tousenList.append(seiribango)
        else:
            driver.get(koenUrl)
        
    # else:
        # driver.get("https://www.fc-member.johnnys-net.jp/logout/")
else:
    print("当落が出ました")
    for rakusen in rakusenList:
        print(F"落選！{rakusen}")
    for tousen in tousenList:
        print(F"当選！{tousen}")
