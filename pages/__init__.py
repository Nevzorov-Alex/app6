from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import datetime
import sys

from abc import ABC, abstractmethod

class Page(ABC):
    __slots__ = ["name","url","headless"]

    def __init__(self,name:str,url:str,headless: bool,path_to_driver:str):
        self.name = name
        self.url=url
        self.headless = headless

    @abstractmethod
    def save_screen_shot(self):
        raise NotImplemented

    @abstractmethod
    def reset_state(self):
        raise NotImplemented

    @abstractmethod
    def quit(selfs):
        raise NotImplemented

class ChromePage(Page):
    __slots__ = ["opts","browser"]

    def __init__(self,name : str,url:str,headless: bool,path_to_driver:str):
        super().__init__(name,url,headless,path_to_driver)

        self.opts=Options()
        self.opts.headless=self.headless
        self.opts.url = self.url


        self.browser = Chrome(executable_path=path_to_driver,options=self.opts)
        self.reset_state()

    def save_screen_shot(self):
        now = datetime.datetime.now()
        self.browser.save_screenshot(f"{self.name}_page.png")

    def reset_state(self):
        self.browser.get(self.url)

    def quit(self):
        self.browser.quit()
