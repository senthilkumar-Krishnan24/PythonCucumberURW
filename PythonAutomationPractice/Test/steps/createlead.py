from _ast import Pass
from openBrowser import *
from src.testproject.sdk.drivers import webdriver 


@given('Create a new lead')
def createNewLead(context):
    #context.driver.find_element_by_xpath("//*[@title='Leads']").is_displayed()
    Pass

@when('Click on the Lead navigation menu')
def moveToLeadNavigationMenu(context):
    #context.driver.find_element_by_xpath("//*[@title='Leads']").click()
    Pass


@when('Click on the New button')
def clickOnNewButton(context):
    Pass


@when('Fill all the required fields on the new lead form')
def FillLeadRequiredFields(context):
    Pass


@when('Click on the Save button')
def clickOnSaveButton(context):
    Pass


@then(u'Verify the lead that converted into account and contact')
def verifyTheLeadConversionIntoAccount(context):
    Pass
