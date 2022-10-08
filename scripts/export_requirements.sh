#!/bin/sh

FILE_NAME_PROD="requirements.txt"
FILE_NAME_DEV="requirements_dev.txt"

echo "Exporting production requirements..."
poetry export -f requirements.txt --output $FILE_NAME_PROD --without-hashes

echo "Exporting development requirements..."
poetry export -f requirements.txt --output $FILE_NAME_DEV --without-hashes --dev

echo "Exported Successfully!"