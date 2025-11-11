Feature: Order Transaction
  Tests related to order Transaction


  Scenario Outline: Verify Order  success Message is shown in details page
    Given place the item order with <user_name> and <password>
    And the user is on landing page

    When I login to portal with <user_name> and <password>
    And navigate to orders page
    And select the orderId

    Then order message is successfully displayed

    Examples:
    |user_name                  | password           |
    |rahulshetty@gmail.com      | Iamking@000        |