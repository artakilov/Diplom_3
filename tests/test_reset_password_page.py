import allure
from pages.reset_password_page import ResetPasswordPage
from pages.forgot_password_page import ForgotPasswordPage


class TestResetPasswordPage:

    # тест 003 - позитивный, клик по кнопке показа/скрытия пароля делает поле активным — подсвечивается
    @allure.title('Проверка, что поле "Пароль" становится активным при клике на кнопку показа/скрытия пароля')
    @allure.description('На странице сброса пароля кликаем на кнопку показа/скрытия пароля. '
                        'Проверяем, что поле становится активным - подсвечивается')
    def test_click_button_show_password(self, driver):
        page = ResetPasswordPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.go_to_forgot_password_page()
        forgot_password_page.set_text_to_field_email()
        forgot_password_page.click_to_button_restore()
        page.click_to_button_password_eye()
        page.check_field_password_is_active()
