Feature: Spectres and managers are able to login to the site

  Scenario: Spectre login and get redirected to reimbursement submission page
    Given The spectre/manager is on the login page
    When The spectre inputs their username
    When The spectre inputs their password
    When The spectre/manager clicks on the login button
    Then The spectre is on the reimbursement submission page

  Scenario: Failed login with wrong information and still on login page
    Given The spectre/manager is on the login page
    When The spectre inputs their username
    When The spectre inputs the wrong password
    When The spectre/manager clicks on the login button
    Then The spectre/manager is still on the login page

  Scenario: Manager login and get redirected to reimbursement management page
    Given The spectre/manager is on the login page
    When The manager inputs their username
    When The manager inputs their password
    When The spectre/manager clicks on the login button
    Then The manager is on the reimbursement management page