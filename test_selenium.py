from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time


WINDOW_SIZE = "1920,1080"


firefox_options = Options()

firefox_options.add_argument("--headless")
firefox_options.add_argument("--window-size=%s" % WINDOW_SIZE)
firefox_options.set_preference("browser.download.folderList", 2)
firefox_options.set_preference("browser.download.dir", r"C:\Users\tians4")
firefox_options.set_preference("browser.download.useDownloadDir", True)
firefox_options.set_preference("browser.download.folderList", 2)
firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")


def test_download_csv():
    browser = webdriver.Firefox(executable_path=r'C:\Users\tians4\geckodriver.exe', firefox_options=firefox_options)
    browser.get("https://jira.cec.lab.emc.com:8443/login.jsp")
    #time.sleep(10)
    browser.implicitly_wait(10)
    elem_login = browser.find_element_by_id("login-form-username")
    elem_login.click()
    elem_login.send_keys("tians4")
    elem_password = browser.find_element_by_id("login-form-password")
    elem_password.click()
    elem_password.send_keys("xxxxxx")
    login_button = browser.find_element_by_id("login-form-submit")
    login_button.click()
    time.sleep(10)
    assert browser.page_source.__contains__('Issues'), 'Login failed'

    issues_button = browser.find_element_by_id("find_link")
    issues_button.click()
    time.sleep(10)
    filter_issue_button = browser.find_element_by_id("filter_lnk_37692_lnk")
    filter_issue_button.click()
    time.sleep(10)
    assert browser.page_source.__contains__('Trident IO MDT list'), 'Export filter MDT page failed'

    export_button = browser.find_element_by_id("AJS_DROPDOWN__25")
    export_button.click()
    time.sleep(10)

    csv_button = browser.find_element_by_id("allCsvFields")
    csv_button.click()
    time.sleep(10)

    confirm_button = browser.find_element_by_id("csv-export-dialog-export-button")
    confirm_button.click()
    time.sleep(10)


if __name__ == "__main__":
    test_download_csv()
