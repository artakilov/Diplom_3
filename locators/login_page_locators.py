from selenium.webdriver.common.by import By


class TestLocatorsLoginPage:

    # ссылка "Восстановить пароль"
    LINK_RESTORE_PASSWORD = By.XPATH, '//a[contains(@href, "/forgot-password")]'
    # поле "email"
    FIELD_EMAIL = By.XPATH, '//input[contains(@name, "name")]'
    # поле "Пароль"
    FIELD_PASSWORD = By.XPATH, '//input[contains(@name, "Пароль")]'
    # кнопка "Войти"
    BUTTON_ENTRANCE = By.XPATH, '//button[contains(text(), "Войти")]'
