import allure
from pages.base_page import BasePage
from locators.login_page_locators import TestLocatorsLoginPage as TLlp
from locators.forgot_password_page_locators import TestLocatorsForgotPasswordPage as TLfpp
import data_for_tests as dft


class LoginPage(BasePage):

    @allure.step('Передаем значение в поле Email')
    def set_text_to_field_email(self, email):
        self.set_text_to_field(TLlp.FIELD_EMAIL, email)

    @allure.step('Передаем значение в поле Пароль')
    def set_text_to_field_password(self, password):
        self.set_text_to_field(TLlp.FIELD_PASSWORD, password)

    @allure.step('Нажимаем кнопку Войти')
    def click_to_button_entrance(self):
        self.click_to_element_with_wait(TLlp.BUTTON_ENTRANCE)

    @allure.step('Авторизуемся пользователем')
    def login_user(self, email, password):
        self.set_text_to_field_email(email)
        self.set_text_to_field_password(password)
        self.click_to_button_entrance()

    @allure.step('Нажимаем ссылку Восстановить пароль')
    def click_link_restore_password(self):
        self.click_to_element_with_wait(TLlp.LINK_RESTORE_PASSWORD)

    @allure.step('Проверяем переход на страницу Восстановления пароля')
    def check_go_to_forgot_password_page(self):
        actually = self.get_text_of_element(TLfpp.BUTTON_RESTORE)
        expected = dft.text_of_button_restore
        assert actually == expected, \
            f'Ожидалась надпись на кнопке: "{expected}", получена: "{actually}"'
