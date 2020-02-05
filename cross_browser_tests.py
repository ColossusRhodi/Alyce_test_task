import traceback


def chrome(webdriver):
    try:
        browser = webdriver.Chrome('path_to_chromedriver.exe') # Add a path to driver.
    except:
        print("Something goes wrong in cross_browser_tests.py file > chrome function. See log file.")
        save = open('log.txt', 'w', encoding='utf-8')
        save.write("cross_browser_tests.py > chrome()" + "\n")
        save.write(traceback.format_exc() + "\n")
        save.close()

    return browser


def firefox(webdriver):
    try:
        browser = webdriver.Firefox(executable_path='path_to_geckodriver.exe',
                                    firefox_binary='path_to_firefox.exe') # Add a path to driver and browser.
    except:
        print("Something goes wrong in cross_browser_tests.py file > firefox function. See log file.")
        save = open('log.txt', 'w', encoding='utf-8')
        save.write("cross_browser_tests.py > firefox()" + "\n")
        save.write(traceback.format_exc() + "\n")
        save.close()

    return browser


def opera(webdriver):
    try:
        browser = webdriver.ChromeOptions()
        browser.binary_location = 'path_to_opera.exe' # Add a path to browser.
        browser = webdriver.Opera(options=browser)
    except:
        print("Something goes wrong in cross_browser_tests.py file > opera function. See log file.")
        save = open('log.txt', 'w', encoding='utf-8')
        save.write("cross_browser_tests.py > opera()" + "\n")
        save.write(traceback.format_exc() + "\n")
        save.close()

    return browser


def edge(webdriver):
    try:
        browser = webdriver.Edge(executable_path='path_to_msedgedriver.exe') # Add a path to driver.
    except:
        print("Something goes wrong in cross_browser_tests.py file > edge function. See log file.")
        save = open('log.txt', 'w', encoding='utf-8')
        save.write("cross_browser_tests.py > edge()" + "\n")
        save.write(traceback.format_exc() + "\n")
        save.close()

    return browser
