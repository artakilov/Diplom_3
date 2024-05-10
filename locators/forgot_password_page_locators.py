from selenium.webdriver.common.by import By


class TestLocatorsForgotPasswordPage:

    # кнопка "Восстановить"
    BUTTON_RESTORE = By.XPATH, '//*[contains(text(), "Восстановить")]'
    # поле "email"
    FIELD_EMAIL = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset/div/div/input'
