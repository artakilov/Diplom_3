from locators.restore_password_page_locators import TestLocatorsRestorePasswordPage as TLrpp
from pages.restore_password_page import RestorePasswordPage
import allure
import constants as cnst
import data_for_tests as dft


class TestRestorePasswordPage:

    # тест 002 - позитивный, ввод почты и клик по кнопке «Восстановить»
    @allure.title('Проверка перехода на страницу сброса пароля при вводе email и по клику на кнопку «Восстановить»')
    @allure.description('На странице восстановления пароля вводим email и кликаем на кнопку "Восстановить". '
                        'Проверяем, что выполнился переход на страницу сброса пароля')
    def test_input_password_and_click_button_restore(self, driver):
        driver.get(cnst.URL + cnst.EP_RESTORE_PASSWORD)
        page = RestorePasswordPage(driver)
        page.set_text_to_field(TLrpp.FIELD_EMAIL, dft.email)
        page.click_to_element_with_wait(TLrpp.BUTTON_RESTORE)

        assert "код из письма" in page.get_text_from_element(TLrpp.LABEL_LETTER), \
            f'Переход на страницу сброса пароля по клику на кнопку "Восстановить" не выполняется!'

    # тест 003 - позитивный, клик по кнопке показа/скрытия пароля делает поле активным — подсвечивается
    @allure.title('Проверка, что поле "Пароль" становится активным при клике на кнопку показа/скрытия пароля')
    @allure.description('На странице сброса пароля кликаем на кнопку показа/скрытия пароля. '
                        'Проверяем, что поле становится активным - подсвечивается')
    def test_click_button_show_password(self, driver):
        driver.get(cnst.URL + cnst.EP_RESTORE_PASSWORD)
        page = RestorePasswordPage(driver)
        page.set_text_to_field(TLrpp.FIELD_EMAIL, dft.email)
        page.click_to_element_with_wait(TLrpp.BUTTON_RESTORE)
        page.set_text_to_field(TLrpp.FIELD_PASSWORD, dft.password)
        page.set_text_to_field(TLrpp.FIELD_LETTER, dft.kod)
        page.click_to_element_with_wait(TLrpp.BUTTON_PASSWORD)

        assert "input_status_active" in page.find_element_with_wait(TLrpp.FIELD_PASSWORD_A).get_attribute("class"), \
            f'Поле не стало активным - не подсвечивается!'
