from pages.account_page import AccountPage
import allure
import constants as cnst
from pages.login_page import LoginPage


class TestAccountPage:

    # тест 004 - позитивный, переход в личный кабинет по клику на кнопку «Личный кабинет» в хедере
    @allure.title('Проверка перехода в личный кабинет по клику на кнопку «Личный кабинет» в хедере')
    @allure.description('Авторизуемся пользователем и кликаем на кнопку "Личный кабинет" в хедере. '
                        'Проверяем, что выполнился переход в личный кабинет')
    def test_go_to_account_page(self, driver, user):
        driver.get(cnst.URL + cnst.EP_LOGIN)
        page = AccountPage(driver)
        login_page = LoginPage(driver)
        login_page.login_user(user["email"], user["password"])
        page.click_to_button_personal_account()
        page.check_go_to_personal_account_page()

    # тест 005 - позитивный, переход в раздел «История заказов» личного кабинета
    @allure.title('Проверка перехода в раздел "История заказов" личного кабинета')
    @allure.description('Авторизуемся пользователем, переходим в личный кабинет и кликаем на раздел "История заказов". '
                        'Проверяем, что выполнился переход в раздел "История заказов"')
    def test_go_to_account_page_history(self, driver, user):
        driver.get(cnst.URL + cnst.EP_LOGIN)
        page = AccountPage(driver)
        login_page = LoginPage(driver)
        login_page.login_user(user["email"], user["password"])
        page.click_to_button_personal_account()
        page.click_to_label_history_orders()
        page.check_go_to_account_page_history()

    # тест 006 - позитивный, выход из аккаунта в личном кабинете
    @allure.title('Проверка выхода из аккаунта в личном кабинета')
    @allure.description('Авторизуемся пользователем, переходим в личный кабинет и кликаем на раздел "Выход". '
                        'Проверяем, что выполнился выход из аккаунта')
    def test_go_to_account_page_exit(self, driver, user):
        driver.get(cnst.URL + cnst.EP_LOGIN)
        page = AccountPage(driver)
        login_page = LoginPage(driver)
        login_page.login_user(user["email"], user["password"])
        page.click_to_button_personal_account()
        page.click_to_label_exit()
        page.check_go_to_account_page_exit()
