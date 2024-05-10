import allure
from pages.base_page import BasePage
from locators.forgot_password_page_locators import TestLocatorsForgotPasswordPage as TLfpp
from locators.reset_password_page_locators import TestLocatorsResetPasswordPage as TLrpp
import data_for_tests as dft


class ForgotPasswordPage(BasePage):

    @allure.step('Передаем значение в поле email')
    def set_text_to_field_email(self):
        self.set_text_to_field(TLfpp.FIELD_EMAIL, dft.email)

    @allure.step('Нажимаем кнопку Восстановить')
    def click_to_button_restore(self):
        self.click_to_element_with_wait(TLfpp.BUTTON_RESTORE)

    @allure.step('Проверяем переход на страницу Ввода нового пароля')
    def check_go_to_reset_password_page(self):
        actually = self.get_text_of_element(TLrpp.BUTTON_SAVE)
        expected = dft.text_of_button_save
        assert actually == expected, \
            f'Ожидалась надпись на кнопке: "{expected}", получена: "{actually}"'
