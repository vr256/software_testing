# Volodymyr_Rizun
A repo for Software Development Technologies course

# WebUI

## Project Structure
- **pages** - contains pages implementing Page Object Model. 
- **features** - contains feature files and also **steps** directory containing **steps_impl.py** - a module performing BDD testing with Behave for given WebUI actions
- **test.py** - performs BDD testing and stores results in **reports** directory
- **reports** - contains html and xml testing reports

## How to Run
It is recommended to set up your virtual environment using **venv** module first, and then follow these steps:
1. git clone https://github.com/VolodymyrRizun/Volodymyr_Rizun.git
2. cd Volodymyr_Rizun
3. git checkout remotes/origin/WebUI
4. Install the required dependencies with   
   `pip install -r requirements.txt`
5. Run the tests with     
   `python -m test`