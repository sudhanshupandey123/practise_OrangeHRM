Feature: OrangeHRM
  Scenario: OrangeHRm PIM Testing
    Given Opening Login_Page of OrangeHRM
    When Enter Username "Admin" and Password "admin123"
    And Entering In PIM
    And Enter FirstName "Mansh" MiddleName "Kumar" LastName "Sahu5"
    And Enter UserName "Mannas12345678910111235689997890abcd" Password "123456789a" and Confirm Password "123456789a"
    Then Verifying Information Saved Or Not
    And Deleting Records