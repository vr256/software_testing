Feature: Delete job title
  As a OrangeHRM user I want to be able to delete job titles, so
  I won't see them on the 'Job titles' page

  Scenario Outline: delete job with given title
      Given I am logged in
      And I am on the 'Job titles' page
      When I delete job with <title>
      Then I should see it <is_visible>

      Examples: Job titles
        | title   | is_visible |
        | Student | False      |
        | Intern  | False      |