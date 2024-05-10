from pages.login_page import LoginPage
import allure
import constants as cnst


class TestLoginPage:

    # тест 001 - позитивный, переход на страницу восстановления пароля по клику на «Восстановить пароль»
    @allure.title('Проверка перехода на страницу восстановления пароля по клику на «Восстановить пароль»')
    @allure.description('На странице входа кликаем на "Восстановить пароль". '
                        'Проверяем, что выполнился переход на страницу восстановления пароля')
    def test_go_to_restore_password_page(self, driver):
        driver.get(cnst.URL + cnst.EP_LOGIN)
        page = LoginPage(driver)
        page.click_link_restore_password()
        page.check_go_to_forgot_password_page()
