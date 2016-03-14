#!/bin/bash

python manage.py makemigrations send_command
python manage.py makemigrations uploader
python manage.py migrate
