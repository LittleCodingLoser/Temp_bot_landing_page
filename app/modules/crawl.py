from textwrap import indent
import time, os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import smtplib

def check_health_leader(health_leader_class, account, password):
    # 外層try except分流帳密根本無法用於登入的狀況
    try:
        # Chrome Driver 路徑
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

        # 進入官網
        driver.get("https://webap1.kshs.kh.edu.tw/kshsSSO/publicWebAP/bodyTemp/bodyTempQuery.aspx")

        # 模擬登陸
        driver.find_element_by_id("ContentPlaceHolder1_txtId").send_keys(account)
        driver.find_element_by_id("ContentPlaceHolder1_txtPassword").send_keys(password)
        driver.find_element_by_id("ContentPlaceHolder1_btnId").click()
        time.sleep(1)

        driver.get("https://webap1.kshs.kh.edu.tw/kshsSSO/publicWebAP/bodyTemp/bodyTempQueryStudent.aspx")
        time.sleep(1)

        # 取得班級
        grade_selection = Select(driver.find_element_by_id("ContentPlaceHolder1_ddlGra")).first_selected_option.get_attribute('value')
        class_selection = Select(driver.find_element_by_id("ContentPlaceHolder1_ddlCla")).first_selected_option.get_attribute('value')

        # 這邊判斷該帳號是否真的屬於該班的環保股長
        if str(health_leader_class) != str(grade_selection) + str(class_selection):
            return -1
        return 1
    except:
        return 0