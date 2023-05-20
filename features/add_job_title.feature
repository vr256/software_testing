Feature: Add job title
  As a OrangeHRM user I want to be able to add job titles, so
  I can see them on the 'Job titles' page

  Scenario Outline: add job title with given data
      Given I am logged in
      And I am on the 'Job titles' page
      And I pressed 'Add job'
      When I add job with <title>, <description>, <note>
      Then I should see it <is_visible>

      Examples: Job titles
        | title   | description | note                        | is_visible |
        | Student | Testing     | WebUI testing with Selenium | True       |
        | Intern  | 123456      | Lorem ipsum dolor sit amet  | True       |