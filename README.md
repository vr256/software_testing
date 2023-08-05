# Testing
A repo for Software Testing course

# WebUI
The goal is to test UI on https://opensource-demo.orangehrmlive.com/web/index.php using Python Selenium client and BDD approach via behave.

## Project Structure
- **pages** - contains pages implementing Page Object Model. BasePage and SidebarPage provides general functionality and are inherited by other page classes. 
- **features** - contains feature files and also **steps** directory containing **steps_impl.py** - a module performing BDD testing with Behave for given WebUI actions. **environment.py** specifies preliminary actions that should be performed before running tests (such as driver acquiring and other set up logics)
- **test.py** - performs BDD testing and stores results in **reports** directory
- **reports** - contains html and xml testing reports

## How to Run
It is recommended to set up your virtual environment using **venv** module first, and then follow these steps:
1. git clone https://github.com/vr256/testing.git
2. cd testing
3. git checkout remotes/origin/WebUI
4. Install the required dependencies with   
   `pip install -r requirements.txt`
5. Specify a browser and run the tests 
   (if no browser provided Chrome would be used)     
   `python -m test edge`