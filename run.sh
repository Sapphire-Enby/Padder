#!/usr/bin/env sh
target='./env/bin/activate'
if [ -e $target ]; then
  source $target
fi
python3 main.py
