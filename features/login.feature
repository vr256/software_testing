Feature: Login
  As a OrangeHRM user I want to be able to enter my username and password, so
  I can login on the website

  Scenario Outline: log in using username and password
      Given I am on the login page
      When I enter <username> and <password>
      And press to login
      Then I should be <logged_in>

      Examples: Pathes
        | username    | password | logged_in |
        | Admin       | admin123 | True      |
        | ADMIN       | admin123 | False     |
        | admin       | 123456   | False     |