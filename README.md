Python with selenium webdriver for system testing

PYTHON VERSION
==============
* *Python Version* - Python 3.7.0
* *Pip Version* - pip 19.3.1 

INSTALL - DRIVERS
=================
If your driver is not compatible with your browser, the testing automation will not be to work.

* Install chromedriver compatible with Chrome
( https://chromedriver.chromium.org/ )

* Install geckodirver compatible with Firefox
( https://github.com/mozilla/geckodriver/releases )

INSTALL - LIBRARIES
===================
sudo pip install behave
sudo pip install pyhamcrest
sudo pip install selenium

CHOOSING YOUR BROWSER
=====================

You can choose your browse in file environment.py.
In method configDriver, you must put: firefox or chrome

Ex:
context.driverQA.configDriver("firefox")
context.driverQA.configDriver("chrome")

RUN
===
behave
behave --tags=-all
behave --tags=all
behave --color