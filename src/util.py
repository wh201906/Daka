from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, WebDriverException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from os import environ
from datetime import datetime, timezone, timedelta
from traceback import print_exc

pageWaitTime = 300
implicitWaitTime = 60
sleepTime = 10

try:
    if bool(environ['CI']) == True:
        print("Env: Github")
        isRemote = True
    else:
        print("Env: Local")
        isRemote = False
except KeyError:
    print("Env: Local")
    isRemote = False

if isRemote == False:
    from secret import *

options = Options()
options.headless = isRemote

yi__b_an = 'Mozilla/5.0 yi' + 'b' + 'an_and' + 'roid/5.0.1'
urlcore = 'heal' + 'thch' + 'ecki' + 'n'
url = 'https' + '://' + urlcore + '.hd' + 'u' + 'he' + 'lp.com'

profile = webdriver.FirefoxProfile()
profile.set_preference("general.user" + "agent.override", yi__b_an)

driver = webdriver.Firefox(firefox_profile=profile, options=options)


def tryClickById(itemId):
    global driver
    locator = (By.ID, itemId)
    WebDriverWait(driver, implicitWaitTime,
                  0.5).until(EC.presence_of_element_located(locator))
    element = driver.find_element_by_id(itemId)
    try:
        element.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", element)


def tryClickByXPath(itemXPath):
    global driver
    locator = (By.XPATH, itemXPath)
    WebDriverWait(driver, implicitWaitTime,
                  0.5).until(EC.presence_of_element_located(locator))
    element = driver.find_element_by_xpath(itemXPath)
    try:
        element.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", element)


def printTime():
    print(datetime.now(timezone(
        timedelta(hours=0))).strftime('%Y-%m-%d %H:%M:%S'),
          end=' ')
