
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.catalog_page import catalog_page
from pages.check_out import checkout_page
from pages.login_page import Login_page
from pages.product_cart import product_page


def test_client_path():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\senin\\PycharmProjects\\resource\\chromedriver.exe')
    print("Start test client path")
    login = Login_page(driver)
    login.autorization()
    ct=catalog_page(driver)
    ct.catalog()
    pc=product_page(driver)
    pc.product_cart()
    ch=checkout_page(driver)
    ch.get_screenshot()
