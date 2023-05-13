Feature: Upload file
  As a Dropbox API user I want to be able to upload files with API calls, so 
  I could store them in my Dropbox account

  Background:
    Given I provided correct access token

  Scenario Outline: upload file using its path
      Given I provided <file_path>
      When I send upload file request
      Then I should receive response with status code <status_code>

      Examples: Pathes
        | file_path                             | status_code |
        | /Volodymyr_Rizun/data/video.mp4       | 200         |
        | /Volodymyr_Rizun/data/text.txt        | 200         |
        | /Volodymyr_Rizun/data/image.png       | 200         |