from selenium.webdriver.common.by import By


class TestLocatorsLoginPage:

    # ссылка "Восстановить пароль"
    LINK_RESTORE_PASSWORD = By.XPATH, '/html/body/div/div/main/div/div/p[2]/a'
    # поле "email"
    FIELD_EMAIL = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
    # поле "Пароль"
    FIELD_PASSWORD = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
    # кнопка "Войти"
    BUTTON_ENTRANCE = By.XPATH, '//*[@id="root"]/div/main/div/form/button'
