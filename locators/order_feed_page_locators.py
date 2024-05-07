from selenium.webdriver.common.by import By


class TestLocatorsOrderFeedPage:
    # надпись "Лента Заказов"
    LABEL_ORDER_FEED = By.XPATH, '//*[@id="root"]/div/main/div/h1'
    # надпись "состав" в окне деталей заказа
    LABEL_COMPOUND = By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div/p[3]'
    # счетчик всех заказаов
    COUNTER_ALL_ORDERS = By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[2]/p[2]'
    # счетчик сегодняшних заказаов
    COUNTER_TODAY_ORDERS = By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[3]/p[2]'
    # область для заказов "В работе"
    MEMO_IN_WORK = By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/ul[2]/li'
    # область для заказов "В работе" с номером заказа
    MEMO_IN_WORK_ORDER = By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/ul[2]/li[contains(text(), "0")]'
    # заказ в ленте заказов
    ORDER_IN_ORDER_FEED = By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]/a'
    # номер последнего заказа в ленте заказов
    NUMBER_ORDER = By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]/a/div[1]/p[1]'
