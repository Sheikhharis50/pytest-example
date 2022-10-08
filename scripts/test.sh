#!/bin/sh

echo "Running all tests...."
coverage run -m pytest src

echo "Generating coverage report...."
coverage report -m

echo "Making html of coverage report...."
coverage html

echo "Opening html report...."
open htmlcov/index.html