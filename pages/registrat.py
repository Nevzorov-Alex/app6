
# import sys
# sys.path.append("app")
# sys.path.append("app.pages")

from pages.__init__ import ChromePage
import time

class RegistratPage(ChromePage):
    def __init__(self,url:str,headless: bool,path_to_driver:str):

        super().__init__("registrat",url,headless,path_to_driver)

    def do_registrat(self,name_log:str,email:str,pwd1:str,pwd2:str):
        el_name_log = self.browser.find_element_by_id("log")
        el_email = self.browser.find_element_by_id("email")
        el_pwd1 = self.browser.find_element_by_id("passw_beg")
        el_pwd2 = self.browser.find_element_by_id("passw_fin")

        el_name_log.clear()
        el_email.clear()
        el_pwd1.clear()
        el_pwd2.clear()

        el_name_log.send_keys(name_log)
        el_email.send_keys(email)
        el_pwd1.send_keys(pwd1)
        el_pwd2.send_keys(pwd2)
        time.sleep(1)
        self.browser.find_element_by_id("regi").click()
        time.sleep(2)
        alert =self.browser.switch_to_alert()
        alert_txt=alert.text
        print(alert_txt)
        alert.accept()