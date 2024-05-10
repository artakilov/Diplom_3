import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import TestLocatorsOrderFeedPage as TLofp
import data_for_tests as dft


class OrderFeedPage(BasePage):

    @allure.step('Нажимаем на Заказ в Ленте заказов')
    def click_to_order_in_order_feed(self):
        self.click_to_element_with_wait(TLofp.ORDER_IN_ORDER_FEED)

    @allure.step('Получаем значение Счетчика выполненных заказов за все время')
    def get_text_of_counter_all_orders(self):
        return self.get_text_of_element(TLofp.COUNTER_ALL_ORDERS)

    @allure.step('Получаем значение Счетчика выполненных заказов за сегодня')
    def get_text_of_counter_today_orders(self):
        return self.get_text_of_element(TLofp.COUNTER_TODAY_ORDERS)

    @allure.step('Получаем значение из поля В работе')
    def get_text_of_memo_orders_in_work(self):
        return self.get_text_of_element(TLofp.MEMO_IN_WORK_ORDER)

    @allure.step('Получаем Номер заказа')
    def get_text_of_number_order(self):
        return self.get_text_of_element(TLofp.NUMBER_ORDER)

    @allure.step('Проверяем открытие описания Заказа')
    def check_open_details_of_order(self):
        actually = self.get_text_of_element(TLofp.LABEL_COMPOUND)
        expected = dft.text_of_label_compound
        assert actually == expected, \
            f'На странице ожидалась надпись: "{expected}", получена: "{actually}"'

    @allure.step('Проверяем увеличение счетчика выполненных заказов за все время')
    def check_counter_all_orders_increased(self, counter_now):
        actually = int(self.get_text_of_counter_all_orders())
        assert actually == counter_now + 1, \
            f'Значение счетчика "Выполнено за все время" не увеличилось!'

    @allure.step('Проверяем увеличение счетчика выполненных заказов за сегодня')
    def check_counter_today_orders_increased(self, counter_now):
        actually = int(self.get_text_of_counter_today_orders())
        assert actually == counter_now + 1, \
            f'Значение счетчика "Выполнено за сегодня" не увеличилось!'

    @allure.step('Проверяем наличие номера оформленного заказа в разделе В работе')
    def check_number_of_order_in_work(self, order):
        i = 0
        while i == 0:
            if str(order) in self.get_text_of_memo_orders_in_work():
                i = order
        assert order == i, \
            f'Номер заказа после его оформления не появился в разделе "В работе"!'

    @allure.step('Проверяем наличие номера оформленного заказа в Ленте заказов')
    def check_number_of_order_in_order_feed(self, order):
        assert str(order) in self.get_text_of_number_order(), \
            f'Заказ не отображается на странице "Лента заказов"!'
