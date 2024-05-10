import allure
import constants as cnst
from pages.forgot_password_page import ForgotPasswordPage


class TestForgotPasswordPage:

    # тест 002 - позитивный, ввод почты и клик по кнопке «Восстановить»
    @allure.title('Проверка перехода на страницу сброса пароля при вводе email и по клику на кнопку «Восстановить»')
    @allure.description('На странице восстановления пароля вводим email и кликаем на кнопку "Восстановить". '
                        'Проверяем, что выполнился переход на страницу сброса пароля')
    def test_input_email_and_click_button_restore(self, driver):
        driver.get(cnst.URL + cnst.EP_FORGOT_PASSWORD)
        page = ForgotPasswordPage(driver)
        page.set_text_to_field_email()
        page.click_to_button_restore()
        page.check_go_to_reset_password_page()
