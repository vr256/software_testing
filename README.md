# Testing
A repo for Software Testing course

# WebAPI
The goal is to test Dropbox API using BDD approach in Python (behave).

## Project Structure
- **src** - contains factory and builders to make DropboxAPI requests. It also contains APIRequest class for encapsulating requests logic and APIRequestDirector class for defining a standard way to call methods of builder to receive a proper request.
- **features** - contains 3 feature files and also **steps** directory containing **steps_impl.py** - a module performing BDD testing with Behave for given API calls
- **test.py** - performs BDD testing and stores results in **reports** directory
- **reports** - contains html and xml testing reports

## How to Run
It is recommended to set up your virtual environment using **venv** module first, and then follow these steps:
1. git clone https://github.com/vr256/testing.git
2. cd testing
3. git checkout remotes/origin/WebAPI
4. Install the required dependencies with   
   `pip install -r requirements.txt`
5. Run the tests with     
   `python -m test`

