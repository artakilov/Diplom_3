from locators.main_page_locators import TestLocatorsMainPage as TLmp
from locators.account_page_locators import TestLocatorsAccountPage as TLap
from locators.order_feed_page_locators import TestLocatorsOrderFeedPage as TLofp
from locators.login_page_locators import TestLocatorsLoginPage as TLlp
from pages.main_page import MainPage
import allure
import constants as cnst


class TestMainPage:

    # тест 004 - позитивный, переход в личный кабинет по клику на кнопку «Личный кабинет» в хедере
    @allure.title('Проверка перехода в личный кабинет по клику на кнопку «Личный кабинет» в хедере')
    @allure.description('Авторизуемся пользователем и кликаем на кнопку "Личный кабинет" в хедере. '
                        'Проверяем, что выполнился переход в личный кабинет')
    def test_go_to_account_page(self, driver, user):
        driver.get(cnst.URL)
        page = MainPage(driver)
        page.user_login(TLmp.BUTTON_PERSONAL_ACCOUNT, TLlp.FIELD_EMAIL, TLlp.FIELD_PASSWORD,
                        TLlp.BUTTON_ENTRANCE, user["email"], user["password"])
        page.click_to_element_with_wait(TLmp.BUTTON_PERSONAL_ACCOUNT)

        assert "Профиль" in page.get_text_from_element(TLap.LABEL_PROFILE), \
            f'Переход в личный кабинет по клику на кнопку "Личный кабинет" в хедере не выполнился!'

    # тест 007 - позитивный, переход в ленту заказов по клику на кнопку «Лента заказов» в хедере
    @allure.title('Проверка перехода в ленту заказов по клику на кнопку «Лента заказов» в хедере')
    @allure.description('Кликаем на кнопку "Лента заказов" в хедере. '
                        'Проверяем, что выполнился переход в ленту заказов')
    def test_go_to_order_feed_page(self, driver):
        driver.get(cnst.URL)
        page = MainPage(driver)
        page.click_to_element_with_wait(TLmp.BUTTON_ORDER_FEED)

        assert "Лента заказов" in page.get_text_from_element(TLofp.LABEL_ORDER_FEED), \
            f'Переход в ленту заказов по клику на кнопку «Лента заказов» в хедере не выполнился!'

    # тест 008 - позитивный, переход в конструктор по клику на кнопку «Конструктор» в хедере
    @allure.title('Проверка перехода в конструктор по клику на кнопку «Конструктор» в хедере')
    @allure.description('Кликаем на кнопку "Лента заказов" в хедере. Кликаем на кнопку "Конструктор" в хедере. '
                        'Проверяем, что выполнился переход в конструктор')
    def test_go_to_main_page(self, driver):
        driver.get(cnst.URL)
        page = MainPage(driver)
        page.click_to_element_with_wait(TLmp.BUTTON_ORDER_FEED)
        page.click_to_element_with_wait(TLmp.BUTTON_CONSTRUCTOR)

        assert "Соберите бургер" in page.get_text_from_element(TLmp.LABEL_ASSEMBLE_BURGER), \
            f'Переход в конструктор по клику на кнопку «Конструктор» в хедере не выполнился!'

    # тест 009 - позитивный, если кликнуть на ингредиент, появится всплывающее окно с деталями
    @allure.title('Проверка появления всплывающего окна с деталями по клику на ингредиент')
    @allure.description('Кликаем на ингредиент. Проверяем, что появилось всплывающее окно с деталями')
    def test_view_details_of_ingredient(self, driver):
        driver.get(cnst.URL)
        page = MainPage(driver)
        page.click_to_element_with_wait(TLmp.IMG_INGREDIENT)

        assert "Детали ингредиента" in page.get_text_from_element(TLmp.LABEL_DETAILS_OF_INGREDIENT), \
            f'Появление всплывающего окна с деталями по клику на ингредиент не выполнилось!'

    # тест 010 - позитивный, всплывающее окно с деталями об ингредиенте закрывается кликом по крестику
    @allure.title('Проверка закрытия всплывающего окна с деталями об ингредиенте по клику на крестик')
    @allure.description('Кликаем на ингредиент. В всплывающем окне с деталями об ингредиенте кликаем на крестик')
    def test_close_details_of_ingredient(self, driver):
        driver.get(cnst.URL)
        page = MainPage(driver)
        page.click_to_element_with_wait(TLmp.IMG_INGREDIENT)
        page.click_to_element_with_wait(TLmp.BUTTON_CLOSE_INGREDIENT)

        assert "Соберите бургер" in page.get_text_from_element(TLmp.LABEL_ASSEMBLE_BURGER), \
            f'Закрытие всплывающего окна с деталями об ингредиенте по клику на крестик не выполнилось!'

    # тест 011 - позитивный, при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается
    @allure.title('Проверка увеличения счетчика ингредиента при его добавлении в заказ')
    @allure.description('Перетаскиваем ингредиент в заказ')
    def test_counter_up_when_ingredient_add(self, driver):
        driver.get(cnst.URL)
        page = MainPage(driver)
        page.drug_and_drop_element(TLmp.IMG_INGREDIENT, TLmp.AREA_OF_ORDER)

        assert int(page.get_text_from_element(TLmp.COUNTER_INGREDIENT)) > 0, \
            f'Увеличение счетчика ингредиента при его добавлении в заказ не выполнилось!'

    # тест 012 - позитивный, залогиненный пользователь может оформить заказ
    @allure.title('Проверка оформления заказа залогиненным пользователем')
    @allure.description('Авторизуемся пользователем, добавляем ингредиент и кликаем на кнопку "Оформить заказ". '
                        'Проверяем, что заказ оформлен')
    def test_order_checkout(self, driver, user):
        driver.get(cnst.URL)
        page = MainPage(driver)
        page.user_login(TLmp.BUTTON_PERSONAL_ACCOUNT, TLlp.FIELD_EMAIL, TLlp.FIELD_PASSWORD,
                        TLlp.BUTTON_ENTRANCE, user["email"], user["password"])
        page.drug_and_drop_element(TLmp.IMG_INGREDIENT, TLmp.AREA_OF_ORDER)
        page.click_to_element_with_wait(TLmp.BUTTON_CHECKOUT)

        assert "Ваш заказ начали готовить" in page.get_text_from_element(TLmp.LABEL_ORDER_STARTED), \
            f'Заказ не оформлен!'
