## Online Store Project

Project of online store where you can add, delete, edit customers, items and orders. In the project the connection to
the database is replaced by mocks. The project was made for a
Automated Testing course at the University of Gdańsk.

## Project Status

Project completed on 30 January 2022

[![CI](https://github.com/mstapaj/TestowanieAutomatyczne_Projekt_II/actions/workflows/tests.yml/badge.svg)](https://github.com/mstapaj/TestowanieAutomatyczne_Projekt_II/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/mstapaj/TestowanieAutomatyczne_Projekt_II/branch/main/graph/badge.svg?token=EX21OEJ0YY)](https://codecov.io/gh/mstapaj/TestowanieAutomatyczne_Projekt_II)

## Technologies Used

- assertpy
- codecov
- coverage
- nose2
- parameterized
- pytest
- setuptools
- tox

## Installation and Setup Instructions

#### Example:

Clone down this repository.

Installation:

`pip install -r requirements.txt`

To Run Test Suite:

`python setup.py test` or `nose2` or `tox`

To Run Test Suite with Coverage:

`nose2 --with-coverage`

## Functionalities

- Database connection is replaced with mocks
- It is possible to add, edit, delete customers, items, orders.
- You can show information about customers, items, orders.
- Appropriate validation when creating customers, items, orders.
- The test libraries assertpy and pytest were used. Various types of assertions (including custom matchers)
  were used in the tests.
- Various types of mocks:
    - Mock (dummy, spy, fake, stub)
    - MagicMock
    - mock_open
    - create_autospec
    - MockProperty
    - custom mocks (without using Mock)
- Parametric tests from the parameterized library have been added to the project.
- CI is added to the project using the Codecov website.
- The TDD methodology was used.