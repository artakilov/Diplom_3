from locators.main_page_locators import TestLocatorsMainPage as TLmp
from locators.account_page_locators import TestLocatorsAccountPage as TLap
from locators.login_page_locators import TestLocatorsLoginPage as TLlp
from pages.account_page import AccountPage
import allure
import constants as cnst


class TestAccountPage:

    # тест 005 - позитивный, переход в раздел «История заказов» личного кабинета
    @allure.title('Проверка перехода в раздел "История заказов" личного кабинета')
    @allure.description('Авторизуемся пользователем, переходим в личный кабинет и кликаем на раздел "История заказов". '
                        'Проверяем, что выполнился переход в раздел "История заказов"')
    def test_go_to_account_page_history(self, driver, user):
        driver.get(cnst.URL)
        page = AccountPage(driver)
        page.user_login(TLmp.BUTTON_PERSONAL_ACCOUNT, TLlp.FIELD_EMAIL, TLlp.FIELD_PASSWORD,
                        TLlp.BUTTON_ENTRANCE, user["email"], user["password"])
        page.click_to_element_with_wait(TLmp.BUTTON_PERSONAL_ACCOUNT)
        page.click_to_element_with_wait(TLap.LABEL_HISTORY_ORDERS)

        assert "link_active" in page.find_element_with_wait(TLap.LABEL_HISTORY_ORDERS).get_attribute("class"), \
            f'Переход в раздел "История заказов" по клику на раздел "История заказов" не выполнился!'

    # тест 006 - позитивный, выход из аккаунта в личном кабинете
    @allure.title('Проверка выхода из аккаунта в личном кабинета')
    @allure.description('Авторизуемся пользователем, переходим в личный кабинет и кликаем на раздел "Выход". '
                        'Проверяем, что выполнился выход из аккаунта')
    def test_go_to_account_page_exit(self, driver, user):
        driver.get(cnst.URL)
        page = AccountPage(driver)
        page.user_login(TLmp.BUTTON_PERSONAL_ACCOUNT, TLlp.FIELD_EMAIL, TLlp.FIELD_PASSWORD,
                        TLlp.BUTTON_ENTRANCE, user["email"], user["password"])
        page.click_to_element_with_wait(TLmp.BUTTON_PERSONAL_ACCOUNT)
        page.click_to_element_with_wait(TLap.LABEL_EXIT)

        assert "Войти" in page.find_element_with_wait(TLlp.BUTTON_ENTRANCE).text, \
            f'Выход из аккаунта по клику на раздел "Выход" не выполнился!'
