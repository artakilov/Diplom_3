from locators.order_feed_page_locators import TestLocatorsOrderFeedPage as TLofp
from locators.main_page_locators import TestLocatorsMainPage as TLmp
from locators.login_page_locators import TestLocatorsLoginPage as TLlp
from locators.account_page_locators import TestLocatorsAccountPage as TLap
from pages.order_feed_page import OrderFeedPage
import allure
import constants as cnst


class TestOrderFeedPage:

    # тест 013 - позитивный, если кликнуть на заказ, откроется всплывающее окно с деталями
    @allure.title('Проверка открытия всплывающего окна с деталями при клике на заказ')
    @allure.description('В ленте заказов кликаем на заказ. '
                        'Проверяем, что появилось всплывающее окно с деталями')
    def test_open_details_of_order(self, driver):
        driver.get(cnst.URL + cnst.EP_OREDR_FEED)
        page = OrderFeedPage(driver)
        page.click_to_element_with_wait(TLofp.ORDER_IN_ORDER_FEED)

        assert "тав" in page.get_text_from_element(TLofp.LABEL_COMPOUND), \
            f'Всплывающее окно с деталями не появилось!'

    # тест 014 - позитивный, при создании нового заказа счётчик Выполнено за всё время увеличивается
    @allure.title('Проверка увеличения значения счетчика "Выполнено за все время" при создании нового заказа')
    @allure.description('Запоминаем текущее значение счетчика, авторизуемся, создаем новый заказ. '
                        'Проверяем, что значение счетчика увеличлось')
    def test_counter_all_orders_increased(self, driver, user):
        driver.get(cnst.URL + cnst.EP_OREDR_FEED)
        page = OrderFeedPage(driver)
        counter_now = int(page.get_text_from_element(TLofp.COUNTER_ALL_ORDERS))
        page.user_login(TLmp.BUTTON_PERSONAL_ACCOUNT, TLlp.FIELD_EMAIL, TLlp.FIELD_PASSWORD,
                        TLlp.BUTTON_ENTRANCE, user["email"], user["password"])
        page.drug_and_drop_element(TLmp.IMG_INGREDIENT, TLmp.AREA_OF_ORDER)
        page.click_to_element_with_wait(TLmp.BUTTON_CHECKOUT)
        page.click_to_element_with_wait(TLmp.BUTTON_CLOSE_ORDER_STARTED)
        page.click_to_element_with_wait(TLmp.BUTTON_ORDER_FEED)

        assert counter_now < int(page.get_text_from_element(TLofp.COUNTER_ALL_ORDERS)), \
            f'Значение счетчика "Выполнено за все время" не увеличилось!'

    # тест 015 - позитивный, при создании нового заказа счётчик Выполнено за сегодня увеличивается
    @allure.title('Проверка увеличения значения счетчика "Выполнено за сегодня" при создании нового заказа')
    @allure.description('Запоминаем текущее значение счетчика, авторизуемся, создаем новый заказ. '
                        'Проверяем, что значение счетчика увеличлось')
    def test_counter_today_orders_increased(self, driver, user):
        driver.get(cnst.URL + cnst.EP_OREDR_FEED)
        page = OrderFeedPage(driver)
        page.scroll_to_element(TLofp.COUNTER_TODAY_ORDERS)
        counter_now = int(page.get_text_from_element(TLofp.COUNTER_TODAY_ORDERS))
        page.user_login(TLmp.BUTTON_PERSONAL_ACCOUNT, TLlp.FIELD_EMAIL, TLlp.FIELD_PASSWORD,
                        TLlp.BUTTON_ENTRANCE, user["email"], user["password"])
        page.drug_and_drop_element(TLmp.IMG_INGREDIENT, TLmp.AREA_OF_ORDER)
        page.click_to_element_with_wait(TLmp.BUTTON_CHECKOUT)
        page.click_to_element_with_wait(TLmp.BUTTON_CLOSE_ORDER_STARTED)
        page.click_to_element_with_wait(TLmp.BUTTON_ORDER_FEED)

        assert counter_now < int(page.get_text_from_element(TLofp.COUNTER_TODAY_ORDERS)), \
            f'Значение счетчика "Выполнено за сегодня" не увеличилось!'

    # тест 016 - позитивный, после оформления заказа его номер появляется в разделе В работе
    @allure.title('Проверка появления номера заказа в разделе "В работе" после его оформления')
    @allure.description('Авторизуемся, создаем новый заказ, запоминаем его номер, переходим в ленту заказов. '
                        'Проверяем, что номер заказа после его оформления появился в разделе "В работе"')
    def test_number_of_order_in_work(self, driver, user):
        driver.get(cnst.URL)
        page = OrderFeedPage(driver)
        page.user_login(TLmp.BUTTON_PERSONAL_ACCOUNT, TLlp.FIELD_EMAIL, TLlp.FIELD_PASSWORD,
                        TLlp.BUTTON_ENTRANCE, user["email"], user["password"])
        page.drug_and_drop_element(TLmp.IMG_INGREDIENT, TLmp.AREA_OF_ORDER)
        page.click_to_element_with_wait(TLmp.BUTTON_CHECKOUT)
        page.wait_not_visibility_9999(TLmp.LABEL_NUMBER_OF_ORDER_STARTED_9999)
        number_of_order_started = page.get_text_from_element(TLmp.LABEL_NUMBER_OF_ORDER_STARTED)
        page.click_to_element_with_wait(TLmp.BUTTON_CLOSE_ORDER_STARTED)
        page.click_to_element_with_wait(TLmp.BUTTON_ORDER_FEED)
        page.wait_visibility_order(TLofp.MEMO_IN_WORK_ORDER)

        assert number_of_order_started in page.get_text_from_element(TLofp.MEMO_IN_WORK), \
            f'Номер заказа после его оформления не появился в разделе "В работе"!'

    # тест 017 - позитивный, заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»
    @allure.title('Проверка отображения заказа пользователя из "Истории заказов" в "Ленте заказов"')
    @allure.description('Авторизуемся, создаем заказ, выбираем номер последнего заказа в "Истории заказов". '
                        'Проверяем, что заказ отображается на странице "Лента заказов"')
    def test_number_order_in_order_feed(self, driver, user):
        driver.get(cnst.URL + cnst.EP_OREDR_FEED)
        page = OrderFeedPage(driver)
        page.user_login(TLmp.BUTTON_PERSONAL_ACCOUNT, TLlp.FIELD_EMAIL, TLlp.FIELD_PASSWORD,
                        TLlp.BUTTON_ENTRANCE, user["email"], user["password"])
        page.drug_and_drop_element(TLmp.IMG_INGREDIENT, TLmp.AREA_OF_ORDER)
        page.click_to_element_with_wait(TLmp.BUTTON_CHECKOUT)
        page.click_to_element_with_wait(TLmp.BUTTON_CLOSE_ORDER_STARTED)
        page.click_to_element_with_wait(TLmp.BUTTON_PERSONAL_ACCOUNT)
        page.click_to_element_with_wait(TLap.LABEL_HISTORY_ORDERS)
        number_last_order = page.get_text_from_element(TLap.NUMBER_ORDER)
        page.click_to_element_with_wait(TLmp.BUTTON_ORDER_FEED)

        assert number_last_order in page.get_text_from_element(TLofp.NUMBER_ORDER), \
            f'Заказ не отображается на странице "Лента заказов"!'
