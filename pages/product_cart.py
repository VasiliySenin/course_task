from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base


class product_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
    # Locators
    add_favorites="//*[@class='button button--empty button--icon button--favorites not-added']"
    add_two="//*[@data-icon='plus']"
    add_basket="//button[@class='button button--primary button--block button--medium']"
    main_word="//div[@class='message-title']"
    go_chekout="//*[@class='button button--secondary button--block button--large']"
    #Getters
    def get_add_favorites(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_favorites)))
    def get_add_two(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_two)))
    def get_add_basket(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.add_basket)))
    def get_main_word(self):
       return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))
    def get_go_chekout(self):
       return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_chekout)))

    #Actions
    def click_add_favorites(self):
        self.get_add_favorites().click()
        print('Add to favorites')
    def click_add_two(self):
        self.get_add_two().click()
        print('Add two phones')
    def click_add_basket(self):
        self.get_add_basket().click()
        print('Add to basket')
    def click_go_chekout(self):
        self.get_go_chekout().click()
        print('Go to check-out')
     #Methods

    def product_cart(self):
        self.get_current_url()
        self.click_add_favorites()
        self.click_add_two()
        self.click_add_basket()
        self.assert_word(self.get_main_word(), 'Товар добавлен в корзину!')
        self.click_go_chekout()

