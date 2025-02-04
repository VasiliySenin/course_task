import datetime
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base


class checkout_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
#Чтобы тест крутился, пропишу в чек-ауте очистку корзины после выполненого скриншота


    # Locators
    button_basket = "//*[@class='user_icons-icon js-user_icons-icon-cart is-active']"
    delite_product="//*[@class='button button--empty button--icon button--medium button--remove']"
    # Getters
    def get_button_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_basket)))

    def get_delite_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delite_product)))


    # Actions
    def click_button_basket(self):
        self.get_button_basket().click()
        print('Go to basket')


    def click_delite_product(self):
        self.get_delite_product().click()
        print('Click delete_product')

    # Methods

    #Делаем скриншот чекаута
    def get_screenshot(self):
        self.get_current_url()
        time.sleep(5)
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        file_path = 'C:\\Users\\senin\\PycharmProjects\\task_upstore24\\screen\\' + name_screenshot
        super().get_screenshot(file_path)
        self.click_button_basket()
        self.click_delite_product()