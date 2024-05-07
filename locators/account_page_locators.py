from selenium.webdriver.common.by import By


class TestLocatorsAccountPage:
    # раздел "Профиль"
    LABEL_PROFILE = By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[1]/a'
    # раздел "История заказов"
    LABEL_HISTORY_ORDERS = By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[2]/a'
    # раздел "Выход"
    LABEL_EXIT = By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button'
    # последний заказ в истории заказов
    ORDER_IN_HISTORY_OF_ORDERS = By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul/li[-1]/a'
    # номер последнего заказа в ленте заказов
    NUMBER_ORDER = By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul/li[1]/a/div[1]/p[1]'
