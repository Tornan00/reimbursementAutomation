from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
import time

@given(u'The spectre/manager is on the login page')
def step_impl(context):
    context.driver.get('C:\\Users\\jpdom\\Desktop\\Project1\\login.html')


@when(u'The spectre inputs their username')
def step_impl(context):
    context.reimbursement_login_page.username_field().send_keys("reaperkiller")


@when(u'The spectre inputs their password')
def step_impl(context):
    context.reimbursement_login_page.password_field().send_keys("n7")


@when(u'The spectre/manager clicks on the login button')
def step_impl(context):
    context.reimbursement_login_page.login_button().click()


@then(u'The spectre is on the reimbursement submission page')
def step_impl(context):
    time.sleep(0.5)
    title = context.driver.title
    print(title)
    assert title == "Spectre Reimbursements"

@when(u'The spectre inputs the wrong password')
def step_impl(context):
    context.reimbursement_login_page.password_field().send_keys("wrong")


@then(u'The spectre/manager is still on the login page')
def step_impl(context):
    time.sleep(0.5)
    title = context.driver.title
    assert title == "Spectre Reimbursement Login"

@when(u'The manager inputs their username')
def step_impl(context):
    context.reimbursement_login_page.username_field().send_keys("manager")


@when(u'The manager inputs their password')
def step_impl(context):
    context.reimbursement_login_page.password_field().send_keys("password")


@then(u'The manager is on the reimbursement management page')
def step_impl(context):
    time.sleep(0.5)
    title = context.driver.title
    print(title)
    assert title == "Spectre Reimbursement Management"
