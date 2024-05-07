from selenium.webdriver.common.by import By


class TestLocatorsRestorePasswordPage:

    # надпись "Восстановление пароля"
    LABEL_RESTORE_PASSWORD = By.XPATH, '//*[@id="root"]/div/main/div/h2'
    # кнопка "Восстановить"
    BUTTON_RESTORE = By.XPATH, '//*[contains(text(), "Восстановить")]'
    # поле "email"
    FIELD_EMAIL = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset/div/div/input'
    # надпись "Пароль"
    LABEL_PASSWORD = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/label'
    # кнопка показа/скрытия пароля
    BUTTON_PASSWORD = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/div'
    # поле "email"
    FIELD_PASSWORD = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
    # поле "email" активно
    FIELD_PASSWORD_A = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div'
    # поле "код из письма"
    FIELD_LETTER = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
    # надпись "Введите код из письма"
    LABEL_LETTER = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/label'
