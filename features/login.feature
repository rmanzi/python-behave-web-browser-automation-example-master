Feature: Login

  Scenario: Make a login with an account already registered
    Given I navigate to the "http://automationpractice.com/index.php"
    When Verify to the "My Store"
    Then Click to the "SIGN_IN"
    When Putting to "EMAIL" "rmanzi_10@testautomation.com"
    When Putting to "PASSWORD" "Rafa#123456"
    When Click to the "LOGIN_SIGN_IN"

  Scenario: Choose items
    Given Click to the "BUTTON_WOMEN"
    When Click to the "TOPS"
    When We must be to buy item(s)
    When Click to the "CHECKOUT"
    When Click to the "PROCEED"
    When Click to the "PROCEED_ADDRESS"
    When Click to the "PROCEED_SHIPPING"
    When Click to the "PAYMENT"
    When Click to the "BUTTON_CONFIRM"
    Then Checkend "step_end"