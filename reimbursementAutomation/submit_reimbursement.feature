Feature: Spectres should be able to view and submit reimbursements

  Scenario: A table is populated with all previously submitted reimbursements
    Given The spectre is on the reimbursement submission page
    Then A table is populated with previous reimbursement requests

  Scenario: Input reimbursement info and submit reimbursement
    Given The spectre is on the reimbursement submission page
    When The spectre types an amount in the amount field
    When The spectre selects a category from category drop down
    When The spectre types a description in description field
    When The spectre clicks on the submit button
    Then A reimbursement request has been submitted