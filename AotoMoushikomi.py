# PythonでSeleniumのwebdriverモジュールをインポート
from selenium import webdriver
# Selectタグを操作できるモジュール
from selenium.webdriver.support.ui import Select
import time

# 申し込みたい公演の申し込みURL
koenUrl = "https://www.fc-member.johnnys-net.jp/performance/applicant/id/709"

# 公演No(ここに申し込みたい公演の番号を設定)
koenNos = [
    "01281J",
    "01282J",
    "02022J",
    "02031J",
    "02032J",
    "02041J",
    "02042J",
    "02172J",
    "02181J",
    "02182J",
    "02222J",
    "02231J",
    "02232J",
    "03252J",
    "03261J",
    "03262J"
]
# 枚数
maisu = 2
# いつでもよいを選択するか(Trueならいつでもよい)
itsudemoOK = True

# ログインしたいユーザーの会員番号を設定
memberIds = [
    "00886551"
]
# 今は同一パスワードのみ対応
password = ["luna1213"]

# 操作するブラウザを開く
driver = webdriver.Chrome()

for memberId in memberIds:
    # ログインページを開く
    driver.get('https://www.fc-member.johnnys-net.jp/login/index/f/JI')

    driver.implicitly_wait(1)

    # ログインIDを入力する
    driver.find_element_by_id("capture_signIn_customerId").send_keys(memberId)

    # パスワードを入力する
    driver.find_element_by_id(
        "capture_signIn_currentPassword").send_keys(password[0])

    # ログインボタンをクリックする
    driver.find_element_by_xpath(
        "//*[@id='capture_signIn_signInForm']/div[2]/div/div/button").click()

    time.sleep(2)

    for koenNo in koenNos:
        # 指定の公演の申し込みページを開く
        driver.get(koenUrl)

        # チェックボックスにチェックを入れる
        clist = driver.find_elements_by_class_name("checkbox")
        for c in clist:
            c.click()

        # 申し込み本ページに遷移する
        driver.find_element_by_id("applicant-link").click()

        # 第一希望を選択する
        Select(driver.find_element_by_id("request1")).select_by_value(koenNo)

        if itsudemoOK:
            # 第四希望を選択する(いつでもよいかのやつ)
            Select(driver.find_element_by_id("request4")
                   ).select_by_index(1 if itsudemoOK else 2)

        # 次へボタンをクリック
        driver.find_element_by_xpath(
            "//*/section/form/div[2]/div/button").click()

        # チケット枚数を選択
        Select(driver.find_element_by_id("qty")).select_by_index(maisu)

        # 次へボタンをクリック
        driver.find_element_by_xpath(
            "//*/section/form/div[2]/div[1]/button").click()

        time.sleep(2)

        # 申し込むボタンをクリック
        driver.find_element_by_xpath(
            "//*/section/form/div[2]/div[1]/button").click()
    else:
        driver.get("https://www.fc-member.johnnys-net.jp/logout/")
else:
    print("申し込み完了！")
