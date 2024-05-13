from selenium.webdriver.common.by import By


class TestLocatorsResetPasswordPage:

    # кнопка "Сохранить"
    BUTTON_SAVE = By.XPATH, '//*[contains(text(), "Сохранить")]'
    # кнопка показа/скрытия пароля
    BUTTON_PASSWORD_EYE = By.XPATH, '//fieldset/div/div/div'
    # поле "password" активно/подсвечивается
    FIELD_PASSWORD_A = By.XPATH, '//fieldset/div/div[contains(@class, "input_status_active")]'
