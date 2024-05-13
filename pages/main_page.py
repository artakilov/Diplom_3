import allure
from pages.base_page import BasePage
from locators.main_page_locators import TestLocatorsMainPage as TLmp
import data_for_tests as dft
import constants as cnst


class MainPage(BasePage):

    @allure.step('Переходим на глвную страницу')
    def go_to_main_page(self):
        self.go_to_url(cnst.URL)

    @allure.step('Нажимаем кнопку Конструктор в хедере')
    def click_to_button_constructor(self):
        self.click_to_element_with_wait(TLmp.BUTTON_CONSTRUCTOR)

    @allure.step('Нажимаем кнопку Личный кабинет в хедере')
    def click_to_button_personal_account(self):
        self.click_to_element_with_wait(TLmp.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Нажимаем кнопку Лента Заказов в хедере')
    def click_to_button_order_feed(self):
        self.click_to_element_with_wait(TLmp.BUTTON_ORDER_FEED)

    @allure.step('Нажимаем на Ингредиент')
    def click_to_ingredient(self):
        self.click_to_element_with_wait(TLmp.IMG_INGREDIENT)

    @allure.step('Нажимаем на кнопку Крестик окна с описанием ингредиента')
    def click_to_button_close_ingredient(self):
        self.click_to_element_with_wait(TLmp.BUTTON_CLOSE_INGREDIENT)

    @allure.step('Нажимаем кнопку Оформить заказ')
    def click_to_button_checkout(self):
        self.click_to_element_with_wait(TLmp.BUTTON_CHECKOUT)

    @allure.step('Перетаскиваем ингредиент в заказ')
    def drug_and_drop_inredient(self):
        self.drug_and_drop_element(TLmp.IMG_INGREDIENT, TLmp.AREA_OF_ORDER)

    @allure.step('Проверяем переход на страницу Лента заказов')
    def check_go_to_order_feed_page(self, text):
        actually = text
        expected = dft.text_of_label_order_feed
        assert actually == expected, \
            f'На странице ожидалась надпись: "{expected}", получена: "{actually}"'

    @allure.step('Проверяем переход на Главную страницу/Конструктор')
    def check_go_to_main_page(self):
        actually = self.get_text_of_element(TLmp.LABEL_ASSEMBLE_BURGER)
        expected = dft.text_of_label_assemble_burger
        assert actually == expected, \
            f'На странице ожидалась надпись: "{expected}", получена: "{actually}"'

    @allure.step('Проверяем просмотр описания Ингредиента')
    def check_view_details_of_ingredient(self):
        actually = self.get_text_of_element(TLmp.LABEL_DETAILS_OF_INGREDIENT)
        expected = dft.text_of_label_details_of_ingredient
        assert actually == expected, \
            f'На странице ожидалась надпись: "{expected}", получена: "{actually}"'

    @allure.step('Проверяем увеличение количества Ингредиента после добавления в заказ')
    def check_counter_up_when_ingredient_add(self):
        actually = int(self.get_text_of_element(TLmp.COUNTER_INGREDIENT))
        expected = dft.value_counter_ingredient
        assert actually == expected, \
            f'Ожидалось значение: "{expected}", получено: "{actually}"'

    @allure.step('Проверяем оформление Заказа')
    def check_order_checkout(self):
        actually = self.get_text_of_element(TLmp.LABEL_ORDER_STARTED)
        expected = dft.text_of_label_order_started
        assert actually == expected, \
            f'На странице ожидалась надпись: "{expected}", получена: "{actually}"'
