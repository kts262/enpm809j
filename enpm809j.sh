#!/bin/bash
# script to autorun flask site for ENPM809J

export FLASK_APP=enpm809.py
/home/enpm809j/project/venv/bin/python3 -m flask run --host=0.0.0.0 &

