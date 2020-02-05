import traceback
import time
import re
import random


def even_or_odd_apples(browser, sprint):
    try:
        persons_with_apples = browser.find_elements_by_css_selector('div.col-12 > ul')
        for person_with_apple in persons_with_apples:
            apples = re.findall(r'Apple\d', person_with_apple.get_attribute('innerHTML'))
            even_apples = 0
            odd_apples = 0
            for apple in apples:
                if int(apple[-1]) % 2 == 0:
                    even_apples += 1
                else:
                    odd_apples += 1
            if even_apples > 0 and odd_apples == 0 or even_apples == 0 and odd_apples > 0:
                test_status = "Test passed."
            else:
                test_status = "Test failed with combination " + str(sprint)
                break
    except:
        print("Something goes wrong in even_and_odd_combinations_test.py file > even_or_odd_apples function. See log file.")
        save = open('log.txt', 'w', encoding='utf-8')
        save.write("odd_combinations_test.py file > even_or_odd_apples()" + "\n")
        save.write("\"Business logic rule №2 - User never can have apples with both odd and even ids\"" + "\n")
        save.write(traceback.format_exc() + "\n")
        save.close()

    return test_status


def possible_clicks_variants(browser):
    try:
        grab_apple_buttons = browser.find_elements_by_css_selector('button.grab-apple')
        apples_in_basket = browser.find_elements_by_css_selector('ul.list-group.basket > li')
        all_possible_clicks_list = []
        fail_try = 0
        flag = False
        while not flag:
            clicks_variant_list = []
            for each in grab_apple_buttons:
                clicks = random.randrange(0, len(apples_in_basket) + 1)
                clicks_variant_list.append(clicks)
            if sum(clicks_variant_list) <= 5:
                if clicks_variant_list not in all_possible_clicks_list:
                    all_possible_clicks_list.append(clicks_variant_list)
                    fail_try = 0
                else:
                    fail_try += 1
                    if len(all_possible_clicks_list) * 2 < fail_try:
                        flag = True
    except:
        print("Something goes wrong in even_and_odd_combinations_test.py file > possible_clicks_variants function. See log file.")
        save = open('log.txt', 'w', encoding='utf-8')
        save.write("even_and_odd_combinations_test.py file > possible_clicks_variants()" + "\n")
        save.write("\"Business logic rule №2 - User never can have apples with both odd and even ids\"" + "\n")
        save.write(traceback.format_exc() + "\n")
        save.close()

    return all_possible_clicks_list


def check_even_and_odd_combinations(browser):
    try:
        all_possible_clicks_list = possible_clicks_variants(browser)

        grab_apple_buttons = browser.find_elements_by_css_selector('button.grab-apple')
        sprint = 0
        while sprint < len(all_possible_clicks_list):
            for grab_apple_button in grab_apple_buttons:
                grab_apple_button_index = grab_apple_buttons.index(grab_apple_button)
                clicks_on_button = all_possible_clicks_list[sprint][grab_apple_button_index]
                clicks = 0
                while clicks < clicks_on_button:
                    grab_apple_button.click()
                    clicks += 1
                    time.sleep(60)

            test_status = even_or_odd_apples(browser, all_possible_clicks_list[sprint])

            free_apples_button = browser.find_element_by_css_selector('a.free-apples')
            free_apples_button.click()
            time.sleep(60)
            sprint += 1
    except:
        print("Something goes wrong in even_and_odd_combinations_test.py file > check_even_and_odd_combinations function. See log file.")
        save = open('log.txt', 'w', encoding='utf-8')
        save.write("even_and_odd_combinations_test.py file > check_even_and_odd_combinations()" + "\n")
        save.write("\"Business logic rule №2 - User never can have apples with both odd and even ids\"" + "\n")
        save.write(traceback.format_exc() + "\n")
        save.close()

    return test_status
