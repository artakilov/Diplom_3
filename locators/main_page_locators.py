from selenium.webdriver.common.by import By


class TestLocatorsMainPage:

    # кнопка "Конструктор" в хедере
    BUTTON_CONSTRUCTOR = By.XPATH, '//p[contains(text(), "Конструктор")]'
    # кнопка "Лента Заказов" в хедере
    BUTTON_ORDER_FEED = By.XPATH, '//p[contains(text(), "Лента Заказов")]'
    # кнопка "Личный кабинет" в хедере
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, '//p[contains(text(), "Личный Кабинет")]'
    # надпись "Соберите бургер"
    LABEL_ASSEMBLE_BURGER = By.XPATH, '//h1[contains(text(), "Соберите бургер")]'
    # картинка ингредиента "Флюоресцентная булка R2-D3"
    IMG_INGREDIENT = By.XPATH, '//a[contains(@href, "61c0c5a71d1f82001bdaaa6d")]/img'
    # надпись "Детали ингредиента"
    LABEL_DETAILS_OF_INGREDIENT = By.XPATH, '//h2[contains(text(), "Детали ингредиента")]'
    # кнопка закрытия окна с информацией об ингредиенте (крестик)
    BUTTON_CLOSE_INGREDIENT = By.XPATH, '//button[contains(@class, "close_modified")]'
    # область заказа
    AREA_OF_ORDER = By.XPATH, '//span[contains(text(), "верх")]'
    # счетчик ингредиента "Флюоресцентная булка R2-D3"
    COUNTER_INGREDIENT = By.XPATH, '//a[contains(@href, "61c0c5a71d1f82001bdaaa6d")]/div/p[contains(@class, "counter")]'
    # кнопка "Оформить заказ" на главной странице
    BUTTON_CHECKOUT = By.XPATH, '//button[contains(text(), "Оформить заказ")]'
    # надпись "Ваш заказ начали готовить"
    LABEL_ORDER_STARTED = By.XPATH, '//p[contains(text(), "Ваш заказ начали готовить")]'
