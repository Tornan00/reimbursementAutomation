from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from poms.reimbursement_login_page import reimbursementLoginPage
from poms.reimbursement_management_page import reimbursementManagementPage
from poms.reimbursement_submission_page import reimbursementSubmissionPage



def before_all(context: Context):
    context.driver = webdriver.Chrome('C:\\Users\\jpdom\\Desktop\\chromedriver.exe')
    context.driver.implicitly_wait(10)
    context.reimbursement_login_page = reimbursementLoginPage(context.driver)
    context.reimbursement_submission_page = reimbursementSubmissionPage(context.driver)
    context.reimbursement_management_page = reimbursementManagementPage(context.driver)

def after_all(context):
    context.driver.quit()