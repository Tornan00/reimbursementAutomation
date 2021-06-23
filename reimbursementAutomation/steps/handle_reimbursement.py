from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from selenium.webdriver.common.alert import Alert


@given(u'The manager is on the reimbursement management page')
def step_impl(context):
    context.driver.get('C:\\Users\\jpdom\\Desktop\\Project1\\manager.html?id=1')
    time.sleep(1)


@then(u'A table is populated with pending reimbursement requests')
def step_impl(context):
    time.sleep(2)
    assert len(context.reimbursement_management_page.reimbursement_table_body()) > 0


@when(u'The manager selects a reimbursement from the table')
def step_impl(context):
    context.reimbursement_management_page.select_button().click()


@then(u'The reimbursement\'s description is shown in the description field')
def step_impl(context):
    assert len(context.reimbursement_management_page.desc_field().text) > 0


@when(u'The manager types a reason for approving or denying the reimbursement')
def step_impl(context):
    context.reimbursement_management_page.reason_field().send_keys("No")


@when(u'The manager clicks on the deny button')
def step_impl(context):
    time.sleep(1)
    context.reimbursement_management_page.deny_button().click()


@then(u'A reimbursement request has been handled')
def step_impl(context):
    time.sleep(1)
    alert = Alert(context.driver)
    alert.accept()

@when(u'The manager clicks on the stats button')
def step_impl(context):
    context.reimbursement_management_page.stats_button().click()


@then(u'The manager is on the stats page')
def step_impl(context):
    time.sleep(0.5)
    title = context.driver.title
    print(title)
    assert title == "Reimbursement Statistics"


