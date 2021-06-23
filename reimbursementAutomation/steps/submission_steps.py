from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from selenium.webdriver.common.alert import Alert


@given(u'The spectre is on the reimbursement submission page')
def step_impl(context):
    context.driver.get('C:\\Users\\jpdom\\Desktop\\Project1\\spectre.html?id=4')
    time.sleep(1)


@when(u'The spectre types an amount in the amount field')
def step_impl(context):
    context.reimbursement_submission_page.amount_field().send_keys("333")


@when(u'The spectre selects a category from category drop down')
def step_impl(context):
    context.reimbursement_submission_page.category_field().select_by_visible_text('Food')



@when(u'The spectre types a description in description field')
def step_impl(context):
    context.reimbursement_submission_page.desc_field().send_keys("Needed to buy a yummy snack")


@when(u'The spectre clicks on the submit button')
def step_impl(context):
    context.reimbursement_submission_page.submission_button().click()

@then(u'A reimbursement request has been submitted')
def step_impl(context):
    time.sleep(1)
    alert = Alert(context.driver)
    alert.accept()

@then(u'A table is populated with previous reimbursement requests')
def step_impl(context):
    time.sleep(2)
    assert len(context.reimbursement_submission_page.reimbursement_table_body()) > 0

