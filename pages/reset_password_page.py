import allure
from pages.base_page import BasePage
from locators.reset_password_page_locators import TestLocatorsResetPasswordPage as TLrpp
import data_for_tests as dft
import constants as cnst


class ResetPasswordPage(BasePage):

    @allure.step('Переходим на глвную страницу')
    def go_to_reset_password_page(self):
        self.go_to_url(cnst.URL + cnst.EP_RESET_PASSWORD)

    @allure.step('Нажимаем кнопку скрытия/показа Пароля')
    def click_to_button_password_eye(self):
        self.click_to_element_with_wait(TLrpp.BUTTON_PASSWORD_EYE)

    @allure.step('Получаем текст кнопки Сохранить')
    def get_text_of_button_save(self):
        return self.get_text_of_element(TLrpp.BUTTON_SAVE)

    @allure.step('Проверяем, что поле Пароль стало активным')
    def check_field_password_is_active(self):
        actually = self.get_attribute_of_element(TLrpp.FIELD_PASSWORD_A, dft.attribute_of_field_password_a)
        expected = dft.value_attribute_of_field_password_a
        assert expected in actually, \
            f'Ожидалось значение аттрибута {dft.attribute_of_field_password_a}: "{expected}", получено: "{actually}"'
