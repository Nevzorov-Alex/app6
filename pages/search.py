from pages.__init__ import ChromePage
import time
import sys
sys.path.append("app")
sys.path.append("app.pages")

class SearchPage(ChromePage):
    def __init__(self,url:str,headless: bool,path_to_driver:str):
        super().__init__("search",url,headless,path_to_driver)

        self.search_btn = self.browser.find_element_by_id("search_do")
        self.search_q_input=self.browser.find_element_by_id("search_q")

        li_lis = self.browser.find_element_by_id("content").\
                            find_elements_by_tag_name("ul")
        print("possible value to search")
        for li in li_lis:
            print(li.text)


    def do_search(self,text):
        search_btn = self.browser.find_element_by_id("search_do")
        search_q_input = self.browser.find_element_by_id("search_q")
        search_q_input.clear()
        search_q_input.send_keys(text)
        search_btn.click()

    def list_values(self):
        li_lis=self.browser.find_element_by_id("content").\
                            find_elements_by_tag_name("ul")
        for li in li_lis:
            print(li.text)