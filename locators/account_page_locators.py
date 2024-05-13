from selenium.webdriver.common.by import By


class TestLocatorsAccountPage:
    # раздел "Профиль"
    LABEL_PROFILE = By.XPATH, '//a[contains(text(), "Профиль")]'
    # раздел "История заказов"
    LABEL_HISTORY_ORDERS = By.XPATH, '//a[contains(text(), "История заказов")]'
    # раздел "Выход"
    LABEL_EXIT = By.XPATH, '//button[contains(text(), "Выход")]'
