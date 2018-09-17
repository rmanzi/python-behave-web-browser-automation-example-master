Feature: Sign In

  Scenario: Make an account
    Given I navigate to the "http://automationpractice.com/index.php"
    When Verify to the "My Store"
    When Click to the "SIGN_IN"
    When Putting to "EMAIL_CREATE" "rmanzi_39@testautomation.com"
    Then Click to the "CREATE_AN_ACCOUNT"

  Scenario: Create an account
    Given Click to the "GENDER_MASC"
    When Putting to "NAME" "Rafael"
    When Putting to "LAST_NAME" "Mani"
    When Putting to "NEW_PASSWORD" "Rafa#123456"
    When Click to "01" "march" "1990"
    When Click to the "NEWSLETTER_OPTION"
    When Putting to "COMPANY" "Automation"
    When Putting to "ADDRESS" "3911 S Figueroa St,Los Angeles"
    When Putting to "ADDRESS_TWO" "Los Angeles Memorial Coliseum - CA 9003"
    When Putting to "CITY" "Los Angeles"
    When Putting to "STATE" "California"
    When Putting to "POST_CODE" "92278"
    When Putting to "COUNTRY" "United States"
    When Putting to "OTHER" "Test Automation"
    When Putting to "PHONE" "+558134314939"
    When Putting to "PHONE_MOBILE" "+5581981619062"
    When Putting to "ALIAS" "3851 S Figueroa St"
    When Click to the "SUBMIT_ACCOUNT"
    Then Check "my-account"




