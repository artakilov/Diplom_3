from pages.login_page import LoginPage
from pages.main_page import MainPage
import allure
import constants as cnst


class TestMainPage:

    # тест 007 - позитивный, переход в ленту заказов по клику на кнопку «Лента заказов» в хедере
    @allure.title('Проверка перехода в ленту заказов по клику на кнопку «Лента заказов» в хедере')
    @allure.description('Кликаем на кнопку "Лента заказов" в хедере. '
                        'Проверяем, что выполнился переход в ленту заказов')
    def test_go_to_order_feed_page(self, driver):
        driver.get(cnst.URL)
        page = MainPage(driver)
        page.click_to_button_order_feed()
        page.check_go_to_order_feed_page()

    # тест 008 - позитивный, переход в конструктор по клику на кнопку «Конструктор» в хедере
    @allure.title('Проверка перехода в конструктор по клику на кнопку «Конструктор» в хедере')
    @allure.description('Кликаем на кнопку "Лента заказов" в хедере. Кликаем на кнопку "Конструктор" в хедере. '
                        'Проверяем, что выполнился переход в конструктор')
    def test_go_to_main_page(self, driver):
        driver.get(cnst.URL + cnst.EP_OREDR_FEED)
        page = MainPage(driver)
        page.click_to_button_constructor()
        page.check_go_to_main_page()

    # тест 009 - позитивный, если кликнуть на ингредиент, появится всплывающее окно с деталями
    @allure.title('Проверка появления всплывающего окна с деталями по клику на ингредиент')
    @allure.description('Кликаем на ингредиент. Проверяем, что появилось всплывающее окно с деталями')
    def test_view_details_of_ingredient(self, driver):
        driver.get(cnst.URL)
        page = MainPage(driver)
        page.click_to_ingredient()
        page.check_view_details_of_ingredient()

    # тест 010 - позитивный, всплывающее окно с деталями об ингредиенте закрывается кликом по крестику
    @allure.title('Проверка закрытия всплывающего окна с деталями об ингредиенте по клику на крестик')
    @allure.description('Кликаем на ингредиент. В всплывающем окне с деталями об ингредиенте кликаем на крестик')
    def test_close_details_of_ingredient(self, driver):
        driver.get(cnst.URL)
        page = MainPage(driver)
        page.click_to_ingredient()
        page.click_to_button_close_ingredient()
        page.check_go_to_main_page()

    # тест 011 - позитивный, при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается
    @allure.title('Проверка увеличения счетчика ингредиента при его добавлении в заказ')
    @allure.description('Перетаскиваем ингредиент в заказ')
    def test_counter_up_when_ingredient_add(self, driver):
        driver.get(cnst.URL)
        page = MainPage(driver)
        page.drug_and_drop_inredient()
        page.check_counter_up_when_ingredient_add()

    # тест 012 - позитивный, залогиненный пользователь может оформить заказ
    @allure.title('Проверка оформления заказа залогиненным пользователем')
    @allure.description('Авторизуемся пользователем, добавляем ингредиент и кликаем на кнопку "Оформить заказ". '
                        'Проверяем, что заказ оформлен')
    def test_order_checkout(self, driver, user):
        driver.get(cnst.URL + cnst.EP_LOGIN)
        page = MainPage(driver)
        login_page = LoginPage(driver)
        login_page.login_user(user["email"], user["password"])
        page.click_to_button_checkout()
        page.check_order_checkout()
