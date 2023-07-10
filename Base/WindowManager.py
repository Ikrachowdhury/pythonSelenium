from selenium import webdriver


class WindowManager:

    def __init__(self, driver):
        self.navigate = driver

    def go_back(self):
        self.navigate.back()

    def go_forward(self):
        self.navigate.forward()

    def refresh_page(self):
        self.navigate.refresh()

    def go_to(self, url):
        self.navigate.get(url)

    def switch_to_tab(self, tab_title):
        windows = self.navigate.window_handles
        for window in windows:
            self.navigate.switch_to.window(window)
            if tab_title == self.navigate.title:
                break

    def scroll_top(self):

        self.navigate.execute_script("window.scrollTo(0, 0);")

    def scroll_to(self, element):
        self.navigate.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

    def scroll_bottom(self):
        self.navigate.execute_script("window.scrollTo(0, document.body.scrollHeight);")
