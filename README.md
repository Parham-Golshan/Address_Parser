# Address Parser
## Overview
Address Parser is a Python Flask application that parses street addresses and extracts the street name and house number. The application provides two endpoints for parsing addresses:

- /parser-simple: Parses simple addresses in the format "street name house number", and returns the street name and house number as separate values.
- /parser-medium: Parses medium addresses in formats like "Am Bächle 23" or "Auf der Vogelwiese 23 b", and returns the street name and house number as separate values.
- /parser-complex: Parses complex addresses that may contain additional information, such as prefix or numeric street names like "Calle 39 No 1540", and returns the street name and house number as separate values.
## Installation
To install Address Parser, follow these steps:

1 - Clone the repository to your local machine. 

2 - Create a virtual environment using Python 3.8 or higher.

3 - Activate the virtual environment.

4 - Install the dependencies by running pip install -r requirements.txt.

## Usage
To run the application, activate the virtual environment and run this command **flask run** in your terminal 
The application will start and listen for incoming requests on port 5000.

## Endpoints
The following methods and endpoints are available for parsing addresses:

### 1 - [POST] /parser-simple

#### Request
**Content-Type**: application/json
**sample input:**

    {
      "input_address": "Street 123"
    }

**Response:**

HTTP/1.1 200 OK
Content-Type: application/json

    {
      "street": "Street",
      "housenumber": "123"
    }

### 2 - [POST] /parser-medium

#### Request

**Content-Type**: application/json

**sample input:**

    {
      "input_address": "Example Street 123 b"
    }

**Response:**

HTTP/1.1 200 OK
Content-Type: application/json

    {
      "street": "Example Street",
      "housenumber": "123 b"
    }

### 3 - [POST] /parser-complex

#### Request

**Content-Type**: application/json

**sample input:**

    {
      "input_address": "Example Street 123 No 456"
    }

**Response:**

HTTP/1.1 200 OK
Content-Type: application/json

    {
      "street": "Example Street 123",
      "housenumber": "No 456"
    }

## Testing the Project
To ensure that the project is working as intended, you can run the unit tests provided in the tests/ directory.
To do this please follow these steps:

1 - run the project by **flask run** command in one terminal

2 - run the tests using **python -m unittest tests.test_parser** in another terminal
