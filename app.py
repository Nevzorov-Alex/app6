
import time
from pages.main import MainPage
from pages.login import LoginPage
from pages.search import SearchPage
from pages.registrat import RegistratPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
opts=Options()
base_url="http://127.0.0.1:8081"
chromedriver_path = "chromedriver"


# mp=MainPage(url=base_url,path_to_driver=chromedriver_path,headless=False)
mp=MainPage(url=base_url,path_to_driver=chromedriver_path,headless=False)
time.sleep(3)
mp.save_screen_shot()
mp.quit()

# login_url=f"{base_url}/login"
# login_page = LoginPage(url=login_url,path_to_driver=chromedriver_path,headless=False)
# time.sleep(3)
# # bad credentials
# login_page.do_login(email="alex",pwd="12345")
# # good credentials
# time.sleep(5)
# login_page.do_login(email="walex",pwd="12345")
# login_page.save_screen_shot()
# login_page.quit()
#
# search_url=f"{base_url}/search"
# search_page = SearchPage(url=search_url,path_to_driver=chromedriver_path,headless=False)
#
# print("############ do search text:a")
# search_page.do_search("a")
# search_page.list_values()
# time.sleep(3)
# print("############ do search text:C")
# search_page.do_search("C")
# search_page.list_values()
# print("############ do search text:")
# search_page.do_search("")
# search_page.list_values()
# search_page.quit()


registrat_url=f"{base_url}/registrat"
registrat_page = RegistratPage(url=registrat_url,path_to_driver=chromedriver_path,headless=False)

time.sleep(3)

 # bad credentials
registrat_page.do_registrat(name_log="no_verif",email="avad@mail.ru",pwd1="12345",pwd2="123456")
# # good credentials
time.sleep(5)
registrat_page.do_registrat(name_log="verif",email="avad@mail.ru",pwd1="12345",pwd2="12345")

registrat_page.save_screen_shot()
registrat_page.quit()
