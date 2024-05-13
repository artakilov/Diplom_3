from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получаем url текущей страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переходим на страницу по url')
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step('Ожидаем появление элемента {locator}')
    def wait_presence_element(self, locator):
        WebDriverWait(self.driver, 8).until(EC.presence_of_element_located(locator))

    @allure.step('Ожидаем видимость элемента {locator}')
    def wait_visibility_element(self, locator):
        WebDriverWait(self.driver, 8).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидаем кликабельность элемента {locator}')
    def wait_clickable_element(self, locator):
        WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable(locator))

    @allure.step('Ищем элемент {locator} c ожиданием его появления и видимости и возвращаем его')
    def find_element_with_wait(self, locator):
        self.wait_presence_element(locator)
        self.wait_visibility_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Получаем аттрибут {attribute} элемента {locator}')
    def get_attribute_of_element(self, locator, attribute):
        return self.find_element_with_wait(locator).get_attribute(attribute)

    @allure.step('Передаем элементу {locator} значение "{text}"')
    def set_text_to_field(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получаем text элемента {locator}')
    def get_text_of_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Нажимаем по элементу {locator} с ожиданием его появления и кликабельности')
    def click_to_element_with_wait(self, locator):
        self.wait_presence_element(locator)
        self.wait_clickable_element(locator)
        while True:
            try:
                self.driver.find_element(*locator).click()
                break
            except ElementClickInterceptedException:
                pass

    @allure.step('Перетаскиваем элемент "{locator_a}" в "{locator_b}"')
    def drug_and_drop_element(self, locator_a, locator_b):
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(self.find_element_with_wait(locator_a),
                                    self.find_element_with_wait(locator_b)).perform()
