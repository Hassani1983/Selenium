from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Driver = webdriver.Chrome(executable_path="C:\\bin\\chromedriver.exe")
Driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# Browser Action 1 > Open Web
Driver.get("https://google.com")
sleep(2)

# # Browser Action 2 > print Title
# Window_title = Driver.title
# print(Window_title)
#
# # Browser Action 3 > Open Web
# Driver.get("http://wikipedia.com")
# sleep(2)
# Driver.back()
# sleep(2)
# Driver.forward()
# sleep(2)
# Driver.refresh()
# sleep(2)

Driver.switch_to.new_window("tab")
Driver.switch_to.new_window('window')
sleep(3)