from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math



link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_element = browser.find_element_by_id('input_value').text


    print(first_element)

    x = first_element
    y = calc(x)

    print(y)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    answer_bt = browser.find_element_by_id("answer").send_keys(y)
    #відсилає значення (у) для поля вводу

    #send_valuex = browser.find_element_by_id("answer").send_keys(y)

    check_box = browser.find_element_by_id("robotCheckbox").click()

    robots_rule = browser.find_element_by_id("robotsRule").click()

    submission = browser.find_element_by_class_name("btn.btn-primary").click()




finally:

    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла