# zw-python-selenium-demo
 A selenium demo in python
 
## Package management: Poetry
Install Poetry:
Mac/Linux:
> curl -sSL https://install.python-poetry.org | python3 -

Windows (powershell):
> (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

Install dependencies from the root of the project with:
> poetry install

Alternatively, if you would rather not use poetry, you can install these packages using pip:
behave 1.2.6, 
behavex 1.5.11, 
selenium 4.4.3


## package explanations:
Behave - a python implementation of the Cucumber BDD framework

Behavex - a behave runner that allows for parallel execution of test among other nice features like reports

Selenium - the tool we're using to automate browser interactions



## Setup:
Three environment variables are required to run tests:

DEMO_TESTS_USERNAME=someusername@example.com

DEMO_TESTS_PASSWORD=somepassword

DEMO_BASE_URL=https://www.hudl.com 

Alternatively, if you would like to not have to set environment variables, you can enter the needed information under the before_all function in /zw-python-selenium-demo/features/environment.py

Webdriver:
This demo assuems that you have chromedirver and that you have the location of your chromedriver set in your system path.


## Running tests:
Run all tests outlined in /zw-python-selenium-demo/features/*.feature sequentially. From the root of the project, run:

> behave

To run a specific test, tag the test by adding @(tag) directly above the scenario name. I like to use @now when running single tests during development. After tagging, specify your tag in the behave command like so:

> behave -k -t "@now"

If a failure occurs (which you can cause by tinkering with the feature file, ex: changing the expected error text in Scenario: Unable to log in with bad password) a screenshot folder will be created and a screenshot of the failure will be saved in /zw-python-selenium-demo/screenshots

Running tests in parallel. This is where the behavex package comes in. Behavex is a wrapper over behave that allows us to easily run tests in parallel. From the root of the project run:

> behavex --parallel-processes 5 --parallel-scheme scenario

After the behavex run, and output folder including a html report is created. To view it, open /zw-python-selenium-demo/output/report.html
If a failure occurred during  the run, you can view the failure screenshot on the html report by clicking the "additional evidence" button in the evidence row for the failed test 
