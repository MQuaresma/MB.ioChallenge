# Mercedes-Benz online shop workflow automator

Tool to automate the workflow of adding an item of merchandise to the basket on the [Mercedes-Benz online shop](https://shop.mercedes-benz.com/en-gb/collection/).

## Dependencies
- Python 3 >=3.4
- [Selenium](https://docs.seleniumhq.org) - for browser automation

## How to Run
The [setup script](setup.sh) automatically checks whether pip is installed and installs it if necessary aswell as installing the Selenium package from pip.
The tool can be executed by running `./main.py` on the terminal.

## Status
Currently the tool only runs on macOS systems due to the use of the [Safari webdriver](https://webkit.org/blog/6900/webdriver-support-in-safari-10/) for the 
[Selenium framework](https://docs.seleniumhq.org).
