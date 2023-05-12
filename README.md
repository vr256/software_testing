# Volodymyr_Rizun
A repo for Software Development Technologies course

# WebAPI

## Project Structure
- **src** contains factory and builders to make DropboxAPI requests. It also contains APIRequest class for encapsulating requests logic and APIRequestDirector class for defining a standard way to call methods of builder to receive a proper request.
- **features** contains 3 feature files and also **steps** directory containing **steps_impl.py** - a module performing BDD testing with Behave for given API calls
- **test.py** performs BDD testing and wraps results using pytest

## How to Run
It is recommended to set up your virtual environment using **venv** module first, and then follow these steps:
1. Install the required dependencies with `pip install -r requirements.txt`
2. Run the tests with `pytest -v -s --html=pytest_report.html test.py`