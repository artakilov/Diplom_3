from locators.login_page_locators import TestLocatorsLoginPage as TLlp
from locators.restore_password_page_locators import TestLocatorsRestorePasswordPage as TLrpp
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
        page.scroll_and_click_to_element(TLlp.LINK_RESTORE_PASSWORD)

        assert "Восстановление пароля" in page.get_text_from_element(TLrpp.LABEL_RESTORE_PASSWORD), \
            f'Переход в "Личный кабинет" по клику на кнопку "Личный кабинет" в хедере не выполняется!'
