from selenium import webdriver


class WindowManager:
    driver = webdriver.Chrome()

    def __init__(self):
        self.navigate = self.driver

    def go_back(self):
        self.navigate.back()

    def go_forward(self):
        self.navigate.forward()

    def refresh_page(self):
        self.navigate.refresh()

    def go_to(self, url):
        self.navigate.get(url)

    def switch_to_tab(self, tab_title):
        windows = self.driver.window_handles
        for window in windows:
            self.driver.switch_to.window(window)
            if tab_title == self.driver.title:
                break
