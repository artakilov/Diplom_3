from selenium.webdriver.common.by import By


class TestLocatorsBasePage:
    # кнопка "Конструктор" в хедере
    BUTTON_CONSTRUCTOR = By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a'
    # кнопка "Лента Заказов" в хедере
    BUTTON_ORDER_FEED = By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[2]/a'
    # кнопка "Личный кабинет" в хедере
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, '//*[@id="root"]/div/header/nav/a'
