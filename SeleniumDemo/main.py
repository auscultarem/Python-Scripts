from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\auscu\\OneDrive\\Documents\\Python Scripts\\SeleniumDemo\\chromedriver.exe")

# driver.get("https://rahulshettyacademy.com/#/index")
# driver.maximize_window() # to maximize window
# print(driver.title)
# print(driver.current_url)
#
# driver.get("https://rahulshettyacademy.com/AutomationPractice1/")
# driver.back() # to return to previous page
# driver.refresh() # to refresh the web page
# driver.minimize_window() # to minimizewindow
# driver.close() # to close a window

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_id("exampleCheck1").click()
