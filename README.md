# Selenium Automated Testing with Python

## Overview

This project is an automated testing framework using Python and Selenium, designed to test the stock data displayed on Google Finance. The framework implements the Page Object Model and Page Factory patterns for better code organization and maintainability.

## Project Structure

├── .github/ │ └── workflows/ │ ├── manual.yml │ └── nightly.yml   
├── requirements.txt    
└── tests/ ├── page_objects/ │ └── finance_page.py └── test_finance.py   

- **.github/**: Contains GitHub Actions workflows for CI/CD.
- **requirements.txt**: Lists the required Python packages for this project.
- **tests/**: Contains the test scripts and page object models.

## Prerequisites

- Python 3.8 or higher
- Google Chrome
- ChromeDriver (automatically handled in CI)

## Run
The project is set up with GitHub Actions for continuous integration. The tests will run automatically on every push and pull request to the main branch.
#### Using Action
Manual Workflow: Allows you to trigger a run of all tests or specific test cases (case 5 and case 6).
- all:
  - Run all the test cases
- case_5_6:
  - Run test case 5 and 6
  - Nightly Workflow: Runs nightly at midnight (UTC)

#### Local Run
- Run all test cases:
  - python -m unittest tests.test_finance.FinanceTest.test_full
- Run test case 5 and 6:
  - python -m unittest tests.test_finance.FinanceTest.test_case_5 tests.test_finance.FinanceTest.test_case_6
