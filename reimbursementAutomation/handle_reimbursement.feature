Feature: Managers should be able to view and handle reimbursements as well as their statistics

  Scenario: A table is populated with all pending reimbursements
    Given The manager is on the reimbursement management page
    Then A table is populated with pending reimbursement requests

  Scenario: A manager can approve or deny a reimbursement and provide a reason
    Given The manager is on the reimbursement management page
    When The manager selects a reimbursement from the table
    Then The reimbursement's description is shown in the description field
    When The manager types a reason for approving or denying the reimbursement
    When The manager clicks on the deny button
    Then A reimbursement request has been handled

  Scenario: A manager can see the statistics of submitted reimbursements
    Given The manager is on the reimbursement management page
    When The manager clicks on the stats button
    Then The manager is on the stats page