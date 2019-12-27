from pages import ChromePage
import time

class LoginPage(ChromePage):
    def __init__(self,url:str,headless: bool,path_to_driver:str):

        super().__init__("login",url,headless,path_to_driver)

    def do_login(self,email:str,pwd:str):
        el_email = self.browser.find_element_by_id("email")
        el_pwd = self.browser.find_element_by_id("password")

        el_email.clear()
        el_pwd.clear()

        el_email.send_keys(email)
        el_pwd.send_keys(pwd)
        time.sleep(1)
        self.browser.find_element_by_id("signin").click()
        time.sleep(1)
        alert =self.browser.switch_to_alert()
        alert_txt=alert.text
        print(alert_txt)
        alert.accept()