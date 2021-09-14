from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from os import environ

try:
    if bool(environ['CI']) == True:
        print("Env: Github")
    else:
        print("Env: Local")
        from secret import *
except KeyError:
    print("Env: Local")
    from secret import *

yi__b_an = 'Mozilla/5.0 yi' + 'b' + 'an_and' + 'roid/5.0.1'

profile = webdriver.FirefoxProfile()
profile.set_preference("general.user" + "agent.override", yi__b_an)

options = Options()
options.headless = False

driver = webdriver.Firefox(firefox_profile=profile, options=options)

def tryClickById(itemId):
    global driver
    locator = (By.ID, itemId)
    WebDriverWait(driver, 5,
                  0.5).until(EC.presence_of_element_located(locator))
    element = driver.find_element_by_id(itemId)
    try:
        element.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", element)


def tryClickByXPath(itemXPath):
    global driver
    locator = (By.XPATH, itemXPath)
    WebDriverWait(driver, 5,
                  0.5).until(EC.presence_of_element_located(locator))
    element = driver.find_element_by_xpath(itemXPath)
    try:
        element.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", element)