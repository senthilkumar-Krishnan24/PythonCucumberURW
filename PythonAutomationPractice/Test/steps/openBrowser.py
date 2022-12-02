from _ast import Pass

from behave import *
from selenium.webdriver.support import expected_conditions
from src.testproject.classes.web_driver_wait import TestProjectWebDriverWait
from src.testproject.sdk.drivers import webdriver
from src.testproject.sdk.drivers.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launch_chrome_browser(context):
    context.driver = webdriver.Chrome(token='2xW7DgT91IA2vmpo0xZpFLTC6dElC2Mf-w-xjSw-xtM1')
      

@when('open the Salesforce login page {Url}')
def openBrowser(context, Url):
    context.driver.get(Url)  
    
@when('enter username {Username} and password {Password}')
def enterUsernameAndPassword(context, Username, Password):
    context.driver.find_element_by_xpath("//*[@id='username']").send_keys(Username)
    context.driver.find_element_by_xpath("//*[@id='password']").send_keys(Password)
    
    
@when('click on Login button')
def clickOnLoginButton(context):
    context.driver.find_element_by_xpath("//*[@id='Login']").click()

@then('verify the landing page')
def verifyLandingPage(context):   
   
    
    waitt = WebDriverWait(context.driver, 1000)
    waitt.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[text()='Home']")), "Found the Home Text on the landing page")
    
    

   
    
    
    