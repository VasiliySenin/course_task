from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base
class catalog_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    # Locators
    button_catalog="//*[@class='hamburger-trigger js-nav-collections-trigger']"
    button_phone="//*[@alt='Смартфоны']"
    brand="//label[@for='filter-value-109849115']"
    more_color="//span[@data-text-first='Ещё варианты']"
    color="//label[@for='filter-value-109849139']"
    color_2="//label[@for='filter-value-217842450']"
    color_3="//label[@for='filter-value-217843485']"
    color_4="//label[@for='filter-value-259806507']"
    gb_512="//label[@for='filter-value-109849130']"
    tb_1="//label[@for='filter-value-109849250']"
    drop="//*[@id='body']/div[1]/div[3]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/select"
    drop_price="//option[@value='price']"
    product="//*[text()='Смартфон Apple iPhone 16 Pro Max 1 ТБ Черный Титан (nano SIM+eSIM)']"
    #Getters
    def get_button_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_catalog)))
    def get_button_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_phone)))
    def get_brand(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.brand)))
    def get_color(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.color)))
    def get_more_color(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.more_color)))
    def get_color_2(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.color_2)))
    def get_color_3(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.color_3)))
    def get_color_4(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.color_4)))
    def get_gb_512(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.gb_512)))
    def get_tb_1(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.tb_1)))
    def get_drop(self):
        element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.drop)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        return element
    def get_drop_price(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.drop_price)))
    # def get_product(self):
    #     return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.product)))
    #Actions
    def click_button_catalog(self):
        self.get_button_catalog().click()
        print('Click button catalog')
    def click_button_phone(self):
        self.get_button_phone().click()
        print('Click button phone')
    def click_brand(self):
        self.get_brand().click()
        print('Set brand')
    def click_color(self):
        self.get_color().click()
        print('Set color')
    def click_more_color(self):
        self.get_more_color().click()
        print('Set more color')
    def click_color_2(self):
        self.get_color_2().click()
        print('Set color 2')
    def click_color_3(self):
        self.get_color_3().click()
        print('Set color 3')
    def click_color_4(self):
        self.get_color_4().click()
        print('Set color 4')
    def click_gb_512(self):
        self.get_gb_512().click()
        print('Set 512 Gb')
    def click_tb_1(self):
        self.get_tb_1().click()
        print('Set 1 tb')
    def click_fillter(self):
        self.get_drop().click()
        print('Open drop')
        self.get_drop_price().click()
        print('Set drop price')
    # def select_product(self):
    #     self.get_product().click()
    #     print('Select product')
    def select_product(self):
        product_element = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.product)))
        product_element.click()
        print('Select product')
    #Methods

    def catalog(self):
        self.get_current_url()
        self.click_button_catalog()
        self.click_button_phone()
        self.click_brand()
        self.click_color()
        self.click_more_color()
        self.click_color_2()
        self.click_color_3()
        self.click_color_4()
        self.click_gb_512()
        self.click_tb_1()
        self.click_fillter()
        self.select_product()

