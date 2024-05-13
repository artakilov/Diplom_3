from selenium.webdriver.common.by import By


class TestLocatorsForgotPasswordPage:

    # кнопка "Восстановить"
    BUTTON_RESTORE = By.XPATH, '//button[contains(text(), "Восстановить")]'
    # поле "email"
    FIELD_EMAIL = By.XPATH, '//input[contains(@name, "name")]'
