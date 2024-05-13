import allure
from pages.order_feed_page import OrderFeedPage
import helpers as hlprs


class TestOrderFeedPage:

    # тест 013 - позитивный, если кликнуть на заказ, откроется всплывающее окно с деталями
    @allure.title('Проверка открытия всплывающего окна с деталями при клике на заказ')
    @allure.description('В ленте заказов кликаем на заказ. '
                        'Проверяем, что появилось всплывающее окно с деталями')
    def test_open_details_of_order(self, driver):
        page = OrderFeedPage(driver)
        page.go_to_order_feed_page()
        page.click_to_order_in_order_feed()
        page.check_open_details_of_order()

    # тест 014 - позитивный, при создании нового заказа счётчик Выполнено за всё время увеличивается
    @allure.title('Проверка увеличения значения счетчика "Выполнено за все время" при создании нового заказа')
    @allure.description('Запоминаем текущее значение счетчика, авторизуемся, создаем новый заказ. '
                        'Проверяем, что значение счетчика увеличлось')
    def test_counter_all_orders_increased(self, driver, user):
        page = OrderFeedPage(driver)
        page.go_to_order_feed_page()
        counter_now = int(page.get_text_of_counter_all_orders())
        hlprs.create_order(user["response"].json()["accessToken"])
        page.check_counter_all_orders_increased(counter_now)

    # тест 015 - позитивный, при создании нового заказа счётчик Выполнено за сегодня увеличивается
    @allure.title('Проверка увеличения значения счетчика "Выполнено за сегодня" при создании нового заказа')
    @allure.description('Запоминаем текущее значение счетчика, авторизуемся, создаем новый заказ. '
                        'Проверяем, что значение счетчика увеличлось')
    def test_counter_today_orders_increased(self, driver, user):
        page = OrderFeedPage(driver)
        page.go_to_order_feed_page()
        counter_now = int(page.get_text_of_counter_today_orders())
        hlprs.create_order(user["response"].json()["accessToken"])
        page.check_counter_today_orders_increased(counter_now)

    # тест 016 - позитивный, после оформления заказа его номер появляется в разделе В работе
    @allure.title('Проверка появления номера заказа в разделе "В работе" после его оформления')
    @allure.description('Авторизуемся, создаем новый заказ, запоминаем его номер, переходим в ленту заказов. '
                        'Проверяем, что номер заказа после его оформления появился в разделе "В работе"')
    def test_number_of_order_in_work(self, driver, user):
        page = OrderFeedPage(driver)
        page.go_to_order_feed_page()
        order = hlprs.create_order(user["response"].json()["accessToken"])
        page.check_number_of_order_in_work(order)

    # тест 017 - позитивный, заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»
    @allure.title('Проверка отображения заказа пользователя из "Истории заказов" в "Ленте заказов"')
    @allure.description('Авторизуемся, создаем заказ, выбираем номер последнего заказа в "Истории заказов". '
                        'Проверяем, что заказ отображается на странице "Лента заказов"')
    def test_number_order_in_order_feed(self, driver, user):
        page = OrderFeedPage(driver)
        page.go_to_order_feed_page()
        order = hlprs.create_order(user["response"].json()["accessToken"])
        page.check_number_of_order_in_order_feed(order)
