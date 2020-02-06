from selenium import webdriver
from one_apple_per_minute_test import one_apple_per_minute
from even_and_odd_combinations_test import check_even_and_odd_combinations
from alert_tests import *
from cross_browser_tests import *
import time


browser = chrome(webdriver)
browser.get('http://hrtest.alycedev.com/')
browser.maximize_window()

test_status = one_apple_per_minute(browser)
print("Business logic rule №1 - Basket never can give more than one apple per minute.", test_status)
test_status = alert_test_1(browser)
print("Alert message - \"Basket can't give more than one apple per five second\".", test_status)
test_status = alert_test_2(browser)
print("Alert message - \"You cant have apples with both odd and even ids, try again\".", test_status)
test_status = alert_test_3(browser)
print("Alert message - \"Apple basket is empty\".", test_status)
test_status = check_even_and_odd_combinations(browser)
print("Business logic rule №2 - User never can have apples with both odd and even ids.", test_status)

time.sleep(1)
browser.close()


browser = firefox(webdriver)
browser.get('http://hrtest.alycedev.com/')
browser.maximize_window()

test_status = one_apple_per_minute(browser)
print("Business logic rule №1 - Basket never can give more than one apple per minute.", test_status)
test_status = alert_test_1(browser)
print("Alert message - \"Basket can't give more than one apple per five second\".", test_status)
test_status = alert_test_2(browser)
print("Alert message - \"You cant have apples with both odd and even ids, try again\".", test_status)
test_status = alert_test_3(browser)
print("Alert message - \"Apple basket is empty\".", test_status)
test_status = check_even_and_odd_combinations(browser)
print("Business logic rule №2 - User never can have apples with both odd and even ids.", test_status)

time.sleep(1)
browser.close()


browser = opera(webdriver)
browser.get('http://hrtest.alycedev.com/')
browser.maximize_window()

test_status = one_apple_per_minute(browser)
print("Business logic rule №1 - Basket never can give more than one apple per minute.", test_status)
test_status = alert_test_1(browser)
print("Alert message - \"Basket can't give more than one apple per five second\".", test_status)
test_status = alert_test_2(browser)
print("Alert message - \"You cant have apples with both odd and even ids, try again\".", test_status)
test_status = alert_test_3(browser)
print("Alert message - \"Apple basket is empty\".", test_status)
test_status = check_even_and_odd_combinations(browser)
print("Business logic rule №2 - User never can have apples with both odd and even ids.", test_status)

time.sleep(1)
browser.close()


browser = edge(webdriver)
browser.get('http://hrtest.alycedev.com/')
browser.maximize_window()

test_status = one_apple_per_minute(browser)
print("Business logic rule №1 - Basket never can give more than one apple per minute.", test_status)
test_status = alert_test_1(browser)
print("Alert message - \"Basket can't give more than one apple per five second\".", test_status)
test_status = alert_test_2(browser)
print("Alert message - \"You cant have apples with both odd and even ids, try again\".", test_status)
test_status = alert_test_3(browser)
print("Alert message - \"Apple basket is empty\".", test_status)
test_status = check_even_and_odd_combinations(browser)
print("Business logic rule №2 - User never can have apples with both odd and even ids.", test_status)

time.sleep(1)
browser.close()
