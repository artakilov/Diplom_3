from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем поялвения номера заказа на старнице нового заказа')
    def wait_not_visibility_9999(self, locator):
        try:
            WebDriverWait(self.driver, 8).until_not(EC.visibility_of_element_located(locator))
        except TimeoutException:
            pass

    @allure.step('Ждем поялвения номера заказа в разделе "В работе"')
    def wait_visibility_order(self, locator):
        try:
            WebDriverWait(self.driver, 8).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            pass

    @allure.step('Ищем элемент {locator} c ожиданием его видимости и возвращаем его')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 8).until(EC.presence_of_element_located(locator))
        WebDriverWait(self.driver, 8).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликаем по элементу {locator} с ожиданием его кликабельности')
    def click_to_element_with_wait(self, locator):
        WebDriverWait(self.driver, 8).until(EC.presence_of_element_located(locator))
        WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable(locator))
        while True:
            try:
                self.driver.find_element(*locator).click()
                break
            except ElementClickInterceptedException:
                pass

    @allure.step('Передаем элементу {locator} значение "{text}" с ожиданием его видимости')
    def set_text_to_field(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получаем text от элемента {locator} с ожиданием его видимости')
    def get_text_from_element(self, locator):
        try:
            return self.find_element_with_wait(locator).text
        except TimeoutException:
            return '9999'

    @allure.step('Прокручиваем страницу до элемента {locator}')
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element_with_wait(locator))

    @allure.step('Прокручиваем страницу до элемента {locator} и кликаем по нему')
    def scroll_and_click_to_element(self, locator):
        self.scroll_to_element(locator)
        self.click_to_element_with_wait(locator)

    @allure.step('Перетаскиваем элемент "{locator_a}" в "{locator_b}"')
    def drug_and_drop_element(self, locator_a, locator_b):
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(self.find_element_with_wait(locator_a),
                                    self.find_element_with_wait(locator_b)).perform()

    @allure.step('Авторизация пользователя "{email}"')
    def user_login(self, locator_a, locator_b, locator_c, locator_d, email, password):
        self.click_to_element_with_wait(locator_a)
        self.set_text_to_field(locator_b, email)
        self.set_text_to_field(locator_c, password)
        self.click_to_element_with_wait(locator_d)
