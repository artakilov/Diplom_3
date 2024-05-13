import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage


class TestLoginPage:

    # тест 001 - позитивный, переход на страницу восстановления пароля по клику на «Восстановить пароль»
    @allure.title('Проверка перехода на страницу восстановления пароля по клику на «Восстановить пароль»')
    @allure.description('На странице входа кликаем на "Восстановить пароль". '
                        'Проверяем, что выполнился переход на страницу восстановления пароля')
    def test_go_to_restore_password_page(self, driver):
        page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        page.go_to_login_page()
        page.click_link_restore_password()
        page.check_go_to_forgot_password_page(forgot_password_page.get_text_of_button_restore())
