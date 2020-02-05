import traceback
import time


def one_apple_per_minute(browser):
    try:
        test_status = "Test passed."
        while time.process_time() < 60:
            grab_apple_button = browser.find_element_by_css_selector('button.grab-apple')
            grab_apple_button.click()
            apples_at_person = browser.find_elements_by_css_selector('div.col-12:nth-child(2) > ul > li')
            if len(apples_at_person) > 1:
                test_status = "Test failed."
                break

        free_apples_button = browser.find_element_by_css_selector('a.free-apples')
        free_apples_button.click()
    except:
        print("Something goes wrong in one_apple_per_minute_test.py file. See log file.")
        save = open('log.txt', 'w', encoding='utf-8')
        save.write("one_apple_per_minute_test.py" + "\n")
        save.write("\"Business logic rule №1 - Basket never can give more than one apple per minute\"" + "\n")
        save.write(traceback.format_exc() + "\n")
        save.close()

    return test_status
