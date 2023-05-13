Feature: Get file metadata
  As a Dropbox API user I want to be able to upload files with API calls, so 
  I could access their information and sharing status

  Background:
    Given I provided correct access token

  Scenario Outline: get file metadata using its path
      Given I provided <file_path>
      When I send get file metadata request
      Then I should receive response with status code <status_code>
      And displayed path <path_display>

      Examples: Pathes
        | file_path                             | status_code |  path_display                         |
        | /Volodymyr_Rizun/data/video.mp4       | 200         | /Volodymyr_Rizun/data/video.mp4       |
        | /Volodymyr_Rizun/data/text.txt        | 200         | /Volodymyr_Rizun/data/text.txt        |
        | /Volodymyr_Rizun/data/image.png       | 200         | /Volodymyr_Rizun/data/image.png       |