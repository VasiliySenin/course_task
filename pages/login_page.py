from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base



class Login_page(Base):
    url='https://upstore24.ru/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
    # Locators
    button_lk="//*[@class='user_icons-item js-user_icons-item nav-hide']"
    field_email="//input[@id='email']"
    feild_password="//input[@id='password']"
    button_enter="//button[@name='commit']"
    main_word="//h1[@class='co-checkout-title co-title co-title--h1']"

    #Getters
    def get_button_lk(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_lk)))
    def get_field_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_email)))
    def get_field_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.feild_password)))
    def get_button_enter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_enter)))
    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    #Actions
    def click_button_lk(self):
        self.get_button_lk().click()
        print('Click button lk')
    def input_field_email(self, field_email):
        self.get_field_email().send_keys(field_email)
        print('Input email')
    def input_field_password(self, fieled_password):
        self.get_field_password().send_keys(fieled_password)
        print('Input field password')
    def click_button_enter(self):
        self.get_button_enter().click()
        print('Click button enter')
    #Methods

    def autorization(self):
        self.driver.delete_all_cookies()  #Без чистки кук почему-то не работает
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_button_lk()
        self.input_field_email('seninvs1989@yandex.ru')
        self.input_field_password('test_task123')
        self.click_button_enter()
        self.assert_word(self.get_main_word(), 'История заказов')
