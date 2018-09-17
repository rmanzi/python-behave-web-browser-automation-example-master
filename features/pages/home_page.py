# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from browser import Browser
from time import sleep

class HomePageLocator(object):
    # Home Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")
    SEARCH_FIELD = (By.ID, "term")
    SUBMIT_BUTTON = (By.ID, "submit")

    """Criando conta de email"""
    SIGN_IN = (By.XPATH, "//*[@id='header']/div[2]/div/div/nav/div[1]/a")
    CREATE_AN_ACCOUNT = (By.ID, "SubmitCreate")

    """Submit Email"""
    EMAIL_CREATE = (By.ID, "email_create")

    """Preenchendo o CRUD - Informacao pessoais"""
    GENDER_MALE = (By.ID, "id_gender1")
    CUSTOMER_FIRST_NAME = (By.ID, "customer_firstname")
    CUSTOMER_LAST_NAME = (By.ID, "customer_lastname")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    DAY = (By.XPATH, "//*[@id ='days']/option[2]")
    MONTHS = (By.XPATH, "//*[@id ='months']/option[4]")
    YEARS = (By.XPATH, "//*[@id='years']/option[30]")

    """"Checkbox para o CRUD"""
    NEWSLETTER = (By.ID, "newsletter")
    OPTION = (By.ID, "optin")

    """CRUD para endereco"""
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    COMPANY = (By.ID, "company")
    ADDRESS = (By.ID, "address1")
    ADDRESS_TWO = (By.ID, "address2")
    CITY = (By.ID, "city")
    STATE = (By.XPATH, "//*[@id='id_state']/option[6]")
    POST_CODE = (By.ID, "postcode")
    COUNTRY = (By.XPATH, "//*[@id='id_country']/option[2]")
    OTHER = (By.ID, "other")
    PHONE = (By.ID, "phone")
    PHONE_MOBILE = (By.ID, "phone_mobile")
    ALIAS = (By.ID, "alias")
    SUBMIT_ACCOUNT = (By.ID, "submitAccount")
    CHECK = (By.ID, "my-account")

    """Login e comprar itens"""
    SUBMIT_LOGIN = (By.ID, "SubmitLogin")
    BUTTON_WOMEN = (By.XPATH, "//*[@id='block_top_menu']/ul/li[1]/a")
    BUTTON_TOPS = (By.XPATH, "//*[@id='categories_block_left']/div/ul/li[1]/a")
    ITEMS = (By.XPATH, "//*[@id='center_column']/ul/li[2]/div/div[2]/h5/a")
    ITEMS_TWO = (By.XPATH, "//*[@id='center_column']/ul/li[1]/div/div[2]/h5/a")
    ADD_CAR = (By.XPATH, "//*[@id='add_to_cart']/button/span")
    BUTTON_PROCEED = (By.XPATH, "//*[@id='layer_cart']/div[1]/div[2]/div[4]/a/span")
    BUTTON_PROCEED_SIGN_IN = (By.XPATH, "//*[@id='center_column']/p[2]/a[1]")
    BUTTON_PROCEED_ADDRESS = (By.XPATH, "//*[@id='center_column']/form/p/button")
    BUTTON_PROCEED_SHIPPING = (By.XPATH, "//*[@id='form']/p/button")
    TERMS_SERVICE = (By.ID, "cgv")
    PAYMENT_BANK = (By.XPATH, "//*[@id='HOOK_PAYMENT']/div[1]/div/p/a")
    BUTTON_CONFIRM = (By.XPATH, "//*[@id='cart_navigation']/button")


class HomePage(Browser):
    # Home Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def search(self, search_term):
        self.fill(search_term, *HomePageLocator.SEARCH_FIELD)
        self.click_element(*HomePageLocator.SUBMIT_BUTTON)

    def click_anythings(self, text):
        if text == "SIGN_IN":
            sleep(5)
            self.click_element(*HomePageLocator.SIGN_IN)
        elif text == "LOGIN_SIGN_IN":
            self.click_element(*HomePageLocator.SUBMIT_LOGIN)
        elif text == "CREATE_AN_ACCOUNT":
            self.click_element(*HomePageLocator.CREATE_AN_ACCOUNT)
        elif text == "GENDER_MASC":
            sleep(5)
            self.click_element(*HomePageLocator.GENDER_MALE)
        elif text == "CHECKOUT":
            sleep(5)
            self.click_element(*HomePageLocator.BUTTON_PROCEED)
        elif text == "PROCEED":
            self.click_element(*HomePageLocator.BUTTON_PROCEED_SIGN_IN)
        elif text == "PROCEED_ADDRESS":
            self.click_element(*HomePageLocator.BUTTON_PROCEED_ADDRESS)
        elif text == "PROCEED_SHIPPING":
            self.click_element(*HomePageLocator.TERMS_SERVICE)
            self.click_element(*HomePageLocator.BUTTON_PROCEED_SHIPPING)
        elif text == "PAYMENT":
            self.click_element(*HomePageLocator.PAYMENT_BANK)
        elif text == "BUTTON_CONFIRM":
            self.click_element(*HomePageLocator.BUTTON_CONFIRM)
        elif text == "TOPS":
            self.click_element(*HomePageLocator.BUTTON_TOPS)
        elif text == "BUTTON_WOMEN":
            self.click_element(*HomePageLocator.BUTTON_WOMEN)
        elif text == "NEWSLETTER_OPTION":
            self.click_element(*HomePageLocator.NEWSLETTER)
            self.click_element(*HomePageLocator.OPTION)
        elif text == "SUBMIT_ACCOUNT":
            self.click_element(*HomePageLocator.SUBMIT_ACCOUNT)


    def insert_anythings(self, text, aux):
        # type: (object, object) -> object
        if text == "COMPANY":
            self.fill(aux, *HomePageLocator.COMPANY)
        elif text == "ADDRESS":
            self.fill(aux, *HomePageLocator.ADDRESS)
        elif text == "ADDRESS_TWO":
            self.fill(aux, *HomePageLocator.ADDRESS_TWO)
        elif text == "CITY":
            self.fill(aux, *HomePageLocator.CITY)
        elif text == "COUNTRY":
            self.click_element(*HomePageLocator.COUNTRY)
        elif text == "STATE":
            sleep(7)
            self.click_element(*HomePageLocator.STATE)
        elif text == "POST_CODE":
            self.fill(aux, *HomePageLocator.POST_CODE)
        elif text == "OTHER":
            self.fill(aux, *HomePageLocator.OTHER)
        elif text == "PHONE":
            self.fill(aux, *HomePageLocator.PHONE)
        elif text == "PHONE_MOBILE":
            self.fill(aux, *HomePageLocator.PHONE_MOBILE)
        elif text == "ALIAS":
            self.fill(aux, *HomePageLocator.ALIAS)
        elif text == "NAME":
            self.fill(aux, *HomePageLocator.CUSTOMER_FIRST_NAME)
        elif text == "LAST_NAME":
            self.fill(aux, *HomePageLocator.CUSTOMER_LAST_NAME)
        elif text == "EMAIL":
            self.fill(aux, *HomePageLocator.EMAIL)
        elif text ==  "PASSWORD":
            self.fill(aux, *HomePageLocator.PASSWORD)
        elif text == "EMAIL_CREATE":
            self.fill(aux, *HomePageLocator.EMAIL_CREATE)
            self.click_element(*HomePageLocator.CREATE_AN_ACCOUNT)
        elif text == "NEW_PASSWORD":
            self.click_element(*HomePageLocator.EMAIL)
            self.fill(aux, *HomePageLocator.PASSWORD)


    def insert_data(self, day, month, year):
        self.click_element(*HomePageLocator.DAY)
        self.click_element(*HomePageLocator.MONTHS)
        self.click_element(*HomePageLocator.YEARS)

    def get_check(self):
        aux = "my-account"
        return aux

    def number_items(self):
        self.click_element(*HomePageLocator.ITEMS)
        self.click_element(*HomePageLocator.ADD_CAR)

    def check_end(self):
        aux = "step_end"
        return aux