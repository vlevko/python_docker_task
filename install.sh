#!/usr/bin/bash

python -m venv env
source env/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
