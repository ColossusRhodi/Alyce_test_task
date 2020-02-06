File test_run.py runs tests for the web app (http://hrtest.alycedev.com/).
Files alert_tests.py, cross_browser_tests.py, even_and_odd_combinations_test.py and one_apple_per_minute_test.py contain an auxiliary function
to test app.

Before running the test_run.py, you must specify paths to browsers and its drivers in the cross_browser_tests.py file!
Drivers for browsers in "drivers" folder!
The necessary part of the code for the change is marked with a comment!

The script is launched by double click on the file test_run.py or from bash.
During the tests execution results, "Test passed." or "Test failed.", will be displayed in terminal.

Tests covering the app in:
	Opening/closeing the app.
	Working the application in four browsers: Google Chrome, Microsoft Edge, Opera and Mozilla Firefox.
	Check the business logic №1 - Basket never can give more than one apple per minute.
	Check the business logic №2 - User never can have apples with both odd and even ids.
	Check all posible variants apples distribution to persons.
	Check all buttons' availableness.
	Check alert texts.

Tools version:
	Python 3.7
	Selenium WebDriver 3.141.0
	Google Chrome 79.0.3945.130 
	chromedriver 79.0.3945.36
	Microsoft Edge 79.0.309.71
	msedgedriver 79.0.309.71
	Mozilla Firefox 72.0.2
	geckodriver 0.26.0
	Opera 66.0.3515.60
	operadriver 79.0.3945.79
