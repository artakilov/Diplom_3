import allure
from pages.base_page import BasePage
from locators.account_page_locators import TestLocatorsAccountPage as TLap
import data_for_tests as dft


class AccountPage(BasePage):

    @allure.step('Нажимаем на раздел История заказов')
    def click_to_label_history_orders(self):
        self.click_to_element_with_wait(TLap.LABEL_HISTORY_ORDERS)

    @allure.step('Нажимаем на раздел Выход')
    def click_to_label_exit(self):
        self.click_to_element_with_wait(TLap.LABEL_EXIT)

    @allure.step('Проверяем переход в раздел Профиль Личного кабинета')
    def check_go_to_personal_account_page(self):
        actually = self.get_text_of_element(TLap.LABEL_PROFILE)
        expected = dft.text_of_label_profile
        assert actually == expected, \
            f'Переход в личный кабинет по нажатию на кнопку "Личный кабинет" в хедере не выполнился!'

    @allure.step('Проверяем переход в раздел История заказов Личного кабинета')
    def check_go_to_account_page_history(self):
        actually = self.get_current_url()
        expected = dft.url_of_label_history_order
        assert actually == expected, \
            f'Переход в раздел "История заказов" по клику на раздел "История заказов" не выполнился!'

    @allure.step('Проверяем Выход из Личного кабинета')
    def check_go_to_account_page_exit(self, text):
        actually = text
        expected = dft.text_of_button_entrance
        assert actually == expected, \
            f'Выход из аккаунта по клику на раздел "Выход" не выполнился!'
