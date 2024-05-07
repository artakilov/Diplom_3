from selenium.webdriver.common.by import By


class TestLocatorsMainPage:
    # кнопка "Конструктор" в хедере
    BUTTON_CONSTRUCTOR = By.XPATH, '//*[contains(text(), "Конструктор")]'
    # кнопка "Лента Заказов" в хедере
    BUTTON_ORDER_FEED = By.XPATH, '//*[contains(text(), "Лента Заказов")]'
    # кнопка "Личный кабинет" в хедере
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, '//*[@id="root"]/div/header/nav/a/p'
    # кнопка "Оформить заказ" на главной странице
    BUTTON_CHECKOUT = By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button'
    # картинка ингредиента "Флюоресцентная булка R2-D3"
    IMG_INGREDIENT = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/img'
    # кнопка закрытия окна с информацией об ингредиенте (крестик)
    BUTTON_CLOSE_INGREDIENT = By.XPATH, '//button[contains(@class, "close_modified")]'
    # счетчик ингредиента "Флюоресцентная булка R2-D3"
    COUNTER_INGREDIENT = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/div[1]/p'
    # надпись "Соберите бургер"
    LABEL_ASSEMBLE_BURGER = By.XPATH, '//*[@id="root"]/div/main/section[1]/h1'
    # идентификатор заказа
    ID_ORDER = By.XPATH, '//*[@id="root"]/div/section/div[1]/div/h2'
    # кнопка "Войти в аккаунт"
    BUTTON_ENTRANCE = By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button'
    # надпись "Детали ингредиента"
    LABEL_DETAILS_OF_INGREDIENT = By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/div/h2'
    # область заказа
    AREA_OF_ORDER = By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]/div/span'
    # надпись "Ваш заказ начали готовить"
    LABEL_ORDER_STARTED = By.XPATH, '//*[@id="root"]/div/section/div[1]/div/div[2]/p[1]'
    # крестик окна нового заказа
    BUTTON_CLOSE_ORDER_STARTED = By.XPATH, '//*[@id="root"]/div/section/div[1]/button'
    # номер оформленного заказа
    LABEL_NUMBER_OF_ORDER_STARTED = By.XPATH, '//*[@id="root"]/div/section/div[1]/div/h2'
    # номер оформленного заказа
    LABEL_NUMBER_OF_ORDER_STARTED_9999 = By.XPATH, '//*[contains(text(), 9999)]'
