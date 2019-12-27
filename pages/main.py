from pages import ChromePage
import datetime
import sys
# sys.path.append("app")
# sys.path.append("app.pages")


class MainPage(ChromePage):
    def __init__(self,url:str,headless: bool,path_to_driver:str):

        super().__init__("main",url,headless,path_to_driver)
        # now = datetime.datetime.now()
        # self.browser.save_screenshot(f"{now}_main_page.png")

    def contact_me_form(self):
        # toDO main
        raise NotImplemented


