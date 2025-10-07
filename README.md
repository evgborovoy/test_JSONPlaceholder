# Automation test framework for JSONPlaceholder

## Project Overview

This project implements a structured REST API automation framework using Python, Pytest and Allure. It is designed to
rigorously validate the functionalities and non-functional requirements (NFRs) of the JSONPlaceholder public API,
specifically targeting the `/posts` resource.

## Installation Steps

Clone the Repository:

```bash
git clone https://github.com/evgborovoy/test_JSONPlaceholder
cd test_JSONPlaceholder
```

## Install Dependencies:

All required libraries (pytest, requests, pydantic, allure-pytest) are listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

## How to run the tests

The framework is configured to run tests using the standard pytest command.

1. Execute All Tests
   To run all functional, negative, and performance tests defined in `tests/test_posts.py`:

```bash
pytest
```

2. Generate and View the Allure Report (Recommended)
   To get detailed, interactive, and professional test results, use Allure reporting:

A. Run Tests with Allure Output
This command executes the tests and generates raw XML/JSON files in the `./allure-results` directory.

```bash
pytest --alluredir=./allure-results
```

B. Serve the Allure Report
After running the tests, use the Allure command-line tool to generate the HTML report and open it in your browser.

Note: You must have the Allure Commandline utility installed on your system to run the allure serve command.

```bash
allure serve allure-results
```

This will automatically open the interactive report, showcasing feature coverage, test duration, and detailed steps for
each test case.

