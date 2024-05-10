from selenium.webdriver.common.by import By


class TestLocatorsMainPage:

    # надпись "Соберите бургер"
    LABEL_ASSEMBLE_BURGER = By.XPATH, '//*[@id="root"]/div/main/section[1]/h1'
    # картинка ингредиента "Флюоресцентная булка R2-D3"
    IMG_INGREDIENT = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/img'
    # надпись "Детали ингредиента"
    LABEL_DETAILS_OF_INGREDIENT = By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/div/h2'
    # кнопка закрытия окна с информацией об ингредиенте (крестик)
    BUTTON_CLOSE_INGREDIENT = By.XPATH, '//button[contains(@class, "close_modified")]'
    # область заказа
    AREA_OF_ORDER = By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]/div/span'
    # счетчик ингредиента "Флюоресцентная булка R2-D3"
    COUNTER_INGREDIENT = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/div[1]/p'
    # кнопка "Оформить заказ" на главной странице
    BUTTON_CHECKOUT = By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button'
    # надпись "Ваш заказ начали готовить"
    LABEL_ORDER_STARTED = By.XPATH, '//*[@id="root"]/div/section/div[1]/div/div[2]/p[1]'
