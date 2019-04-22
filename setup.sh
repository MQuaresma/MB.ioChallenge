#!/bin/bash

if test ! $(which pip); then
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
fi

pip install -U pip

if test ! $(pip list | grep selenium); then
    pip install selenium
fi

chmod +x main.py

echo "Setup complete"
echo "To run type ./main.py on the terminal"
