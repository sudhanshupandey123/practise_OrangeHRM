Feature: OrangeHRM

  Scenario: OrangeHRm PIM Testing
    Given Opening Login_Page of OrangeHRM
    When Login By Using Username "Admin" and Password "admin123"
    And Entering In PIM
    And Enter First_Name "Manash" Middle_Name "Kumar" and Last_Name "Babu"
    And Enter UserName "KPMannas6" Password "123456789a" and Confirm Password "123456789a"
    Then Deleting Records


