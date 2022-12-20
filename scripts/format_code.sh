#!/bin/bash

THERE_IS_NO_CONFIGURATION_FILE='There is no configuration file.'


if [ ! -f ./pyproject.toml ] || [ ! -f ./.isort.cfg ]
then
  echo -e "\n\033[31m${THERE_IS_NO_CONFIGURATION_FILE}\033[0m\n"
else
  isort . && echo '/n'; black .
fi
