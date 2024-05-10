from selenium.webdriver.common.by import By


class TestLocatorsResetPasswordPage:

    # кнопка "Сохранить"
    BUTTON_SAVE = By.XPATH, '//*[contains(text(), "Сохранить")]'
    # кнопка показа/скрытия пароля
    BUTTON_PASSWORD_EYE = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/div'
    # поле "password" активно/подсвечивается
    FIELD_PASSWORD_A = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div'
