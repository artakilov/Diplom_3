from selenium.webdriver.common.by import By


class TestLocatorsOrderFeedPage:

    # надпись "Лента Заказов"
    LABEL_ORDER_FEED = By.XPATH, '//h1[contains(text(), "Лента заказов")]'
    # последний заказ в ленте заказов
    ORDER_IN_ORDER_FEED = By.XPATH, '//ul[contains(@class, "OrderFeed_list")]/li[last()-49]'
    # счетчик всех заказаов
    COUNTER_ALL_ORDERS = By.XPATH, '//div[contains(@class, "undefined")]/p[contains(@class, "OrderFeed_number")]'
    # счетчик сегодняшних заказаов
    COUNTER_TODAY_ORDERS = By.XPATH, '//p[contains(text(), "сегодня")]/following-sibling::p[contains(@class, "digits")]'
    # область для заказов "В работе" с номером заказа
    MEMO_IN_WORK_ORDER = By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li'
    # номер последнего заказа в ленте заказов
    NUMBER_ORDER = By.XPATH, '//ul[contains(@class, "list")]/li[last()-49]/a/div/p[contains(@class, "digits")]'
    # надпись "состав" в окне деталей заказа
    LABEL_COMPOUND = By.XPATH, '//p[contains(text(), "Cостав")]'
