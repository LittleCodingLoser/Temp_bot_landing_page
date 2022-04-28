from textwrap import indent
import time, os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import smtplib

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def crawl_temp_data(account, password):
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

        # 取得資料
        page = driver.page_source
        driver.quit()
        os.system("cls")
        # 建表
        tables = pd.read_html(page)
        tables = tables[4]
        tables.index += 1
        return tables
    except:
        print("Fail to crawl data")

