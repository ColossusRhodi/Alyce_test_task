import traceback
import time


def alert_test_1(browser):
    try:
        test_status = "Test failed."
        grab_apple_button = browser.find_element_by_css_selector('button.grab-apple')
        grab_apple_button.click()
        grab_apple_button.click()
        time.sleep(1)
        alert = browser.find_element_by_css_selector('div.col-12.alerts')
        if alert.text == "Basket cant give more than one apple per 5 sec":
            test_status = "Test passed."

        free_apples_button = browser.find_element_by_css_selector('a.free-apples')
        free_apples_button.click()
    except:
        print("Something goes wrong in alert_test.py file > alert_test_1. See log file.")
        save = open('log.txt', 'w', encoding='utf-8')
        save.write("alert_test.py file > alert_test_1" + "\n")
        save.write("\"Alert message - \'Basket cant give more than one apple per 5 sec\'\"" + "\n")
        save.write(traceback.format_exc() + "\n")
        save.close()

    return test_status


def alert_test_2(browser):
    try:
        test_status = "Test failed."
        while time.process_time() < 180:
            grab_apple_button = browser.find_element_by_css_selector('button.grab-apple')
            grab_apple_button.click()
            time.sleep(1)
            alert = browser.find_element_by_css_selector('div.col-12.alerts')
            if alert.text == "You cant have apples with both odd and even ids, try again":
                test_status = "Test passed."
                break
            else:
                time.sleep(60)

        free_apples_button = browser.find_element_by_css_selector('a.free-apples')
        free_apples_button.click()
    except:
        print("Something goes wrong in alert_test.py file > alert_test_2. See log file.")
        save = open('log.txt', 'w', encoding='utf-8')
        save.write("alert_test.py file > alert_test_2" + "\n")
        save.write("\"Alert message - \'You cant have apples with both odd and even ids, try again\'\"" + "\n")
        save.write(traceback.format_exc() + "\n")
        save.close()

    return test_status


def alert_test_3(browser):
    try:
        test_status = "Test failed."
        grab_apple_buttons = browser.find_elements_by_css_selector('button.grab-apple')
        apples_in_basket = browser.find_elements_by_css_selector('ul.list-group.basket > li')
        clicks = 0
        while clicks < len(apples_in_basket):
            for button in grab_apple_buttons:
                button.click()
                time.sleep(1)
                alert = browser.find_element_by_css_selector('div.col-12.alerts')
                if alert.text == "Apple basket is empty":
                    test_status = "Test passed."
                else:
                    clicks += 1
                    time.sleep(60)

        free_apples_button = browser.find_element_by_css_selector('a.free-apples')
        free_apples_button.click()
    except:
        print("Something goes wrong in alert_test.py file > alert_test_3. See log file.")
        save = open('log.txt', 'w', encoding='utf-8')
        save.write("alert_test.py file > alert_test_3" + "\n")
        save.write("\"Alert message - \'Apple basket is empty\'\"" + "\n")
        save.write(traceback.format_exc() + "\n")
        save.close()

    return test_status
