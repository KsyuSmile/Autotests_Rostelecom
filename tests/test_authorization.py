from config import valid_phone, valid_email, valid_login, valid_pass, valid_ls, invalid_phone, invalid_email


<<<<<<< HEAD
def test_auth_by_phone_valid(browser, auth_elements, button_exit):
=======
def test_auth_by_phone_valid(auth_elements, button_exit):
>>>>>>> 9e2064e (Initial commit)
    """Проверка авторизации по номеру телефона с валидными данными"""

    auth_elements.go_to_site()
    auth_elements.input_username().send_keys(valid_phone)
    auth_elements.input_password().send_keys(valid_pass)
    auth_elements.click_button_to_enter()
    assert button_exit.check_button_exit() == "Выйти"


<<<<<<< HEAD
def test_auth_by_email_valid(browser, auth_elements, button_exit, auth_tab):
=======
def test_auth_by_email_valid(auth_elements, button_exit, auth_tab):
>>>>>>> 9e2064e (Initial commit)
    """Проверяем авторизацию по адресу электронной почты с валидными данными"""

    auth_elements.go_to_site()
    auth_tab.click_tab_email()
    auth_elements.input_username().send_keys(valid_email)
    auth_elements.input_password().send_keys(valid_pass)
    auth_elements.click_button_to_enter()
    assert button_exit.check_button_exit() == "Выйти"


<<<<<<< HEAD
def test_auth_by_login_valid(browser, auth_elements, button_exit, auth_tab):
=======
def test_auth_by_login_valid(auth_elements, button_exit, auth_tab):
>>>>>>> 9e2064e (Initial commit)
    """Проверяем авторизацию по логину с валидными данными"""

    auth_elements.go_to_site()
    auth_tab.click_tab_login()
    auth_elements.input_username().send_keys(valid_login)
    auth_elements.input_password().send_keys(valid_pass)
    auth_elements.click_button_to_enter()
    assert button_exit.check_button_exit() == "Выйти"


<<<<<<< HEAD
def test_auth_by_ls_valid(browser, auth_elements, button_exit, auth_tab):
=======
def test_auth_by_ls_valid(auth_elements, button_exit, auth_tab):
>>>>>>> 9e2064e (Initial commit)
    """Проверяем авторизацию по лицевому счёту с валидными данными"""

    auth_elements.go_to_site()
    auth_tab.click_tab_login()
    auth_elements.input_username().send_keys(valid_ls)
    auth_elements.input_password().send_keys(valid_pass)
    auth_elements.click_button_to_enter()
    assert button_exit.check_button_exit() == "Выйти"


<<<<<<< HEAD
def test_auth_empty_value(browser, auth_elements, error_message):
=======
def test_auth_empty_value(auth_elements, error_message):
>>>>>>> 9e2064e (Initial commit)
    """Проверяем авторизацию с пустыми полями для ввода"""

    auth_elements.go_to_site()
    auth_elements.input_username().send_keys("")
    auth_elements.input_password().send_keys("")
    auth_elements.click_button_to_enter()
    assert error_message.error_message_username() == "Введите номер телефона"


<<<<<<< HEAD
def test_auth_by_phone_invalid(browser, auth_elements, error_message):
=======
def test_auth_by_phone_invalid(auth_elements, error_message):
>>>>>>> 9e2064e (Initial commit)
    """Проверяем авторизацию по номеру телефона с неавторизованным номером телефона"""

    auth_elements.go_to_site()
    auth_elements.input_username().send_keys(invalid_phone)
    auth_elements.input_password().send_keys(valid_pass)
    auth_elements.click_button_to_enter()
    assert error_message.error_message_login_end_pass() == "Неверный логин или пароль"


<<<<<<< HEAD
def test_auth_by_email_invalid(browser, auth_elements, auth_tab, error_message):
=======
def test_auth_by_email_invalid(auth_elements, auth_tab, error_message):
>>>>>>> 9e2064e (Initial commit)
    """Проверяем авторизацию по адресу электронной почты с неавторизованной почтой"""

    auth_elements.go_to_site()
    auth_tab.click_tab_email()
    auth_elements.input_username().send_keys(invalid_email)
    auth_elements.input_password().send_keys(valid_pass)
    auth_elements.click_button_to_enter()
    assert error_message.error_message_login_end_pass() == "Неверный логин или пароль"


<<<<<<< HEAD
def test_click_button_register(browser, auth_elements, register_page):
=======
def test_click_button_register(auth_elements, register_page):
>>>>>>> 9e2064e (Initial commit)
    """Проверяем кнопку 'Зарегистрироваться', переход на страницу регистрыции"""

    auth_elements.go_to_site()
    auth_elements.button_register().click()
    assert register_page.check_section_title() == "Регистрация"


<<<<<<< HEAD
def test_click_button_forgot_pass(browser, auth_elements, recovery_pass_page):
=======
def test_click_button_forgot_pass(auth_elements, recovery_pass_page):
>>>>>>> 9e2064e (Initial commit)
    """Проверяем кнопку 'Забыл пароль', переход на страницу восстановления пароля"""

    auth_elements.go_to_site()
    auth_elements.button_forgot_pass().click()
    assert recovery_pass_page.check_section_title_pass() == "Восстановление пароля"


<<<<<<< HEAD
def test_auth_email_auto_change_tab_from_phone(browser, auth_elements, auth_tab_active):
=======
def test_auth_email_auto_change_tab_from_phone(auth_elements, auth_tab_active):
>>>>>>> 9e2064e (Initial commit)
    """Проверка автоматической смены таба выбора аутентификации при вводе электронной почты из вкладки Телефон"""

    auth_elements.go_to_site()
    auth_elements.input_username().send_keys(valid_email)
    auth_elements.input_password().click()
    assert auth_tab_active.check_tab_email() == "Почта"


<<<<<<< HEAD
def test_auth_login_auto_change_tab_from_phone(browser, auth_elements, auth_tab_active):
=======
def test_auth_login_auto_change_tab_from_phone(auth_elements, auth_tab_active):
>>>>>>> 9e2064e (Initial commit)
    """Проверка автоматической смены таба выбора аутентификации при вводе логина из вкладки Телефон"""

    auth_elements.go_to_site()
    auth_elements.input_username().send_keys(valid_login)
    auth_elements.input_password().click()
    assert auth_tab_active.check_tab_login() == "Логин"


<<<<<<< HEAD
def test_auth_ls_auto_change_tab_from_phone(browser, auth_elements, auth_tab_active):
=======
def test_auth_ls_auto_change_tab_from_phone(auth_elements, auth_tab_active):
>>>>>>> 9e2064e (Initial commit)
    """Проверка автоматической смены таба выбора аутентификации при вводе лицевого счёта из вкладки Телефон"""

    auth_elements.go_to_site()
    auth_elements.input_username().send_keys(valid_ls)
    auth_elements.input_password().click()
    assert auth_tab_active.check_tab_ls() == "Лицевой счёт"


<<<<<<< HEAD
def test_auth_phone_auto_change_tab_from_email(browser, auth_elements, auth_tab, auth_tab_active):
=======
def test_auth_phone_auto_change_tab_from_email(auth_elements, auth_tab, auth_tab_active):
>>>>>>> 9e2064e (Initial commit)
    """Проверка автоматической смены таба выбора аутентификации при вводе номера телефона из вкладки Почта"""

    auth_elements.go_to_site()
    auth_tab.click_tab_email()
    auth_elements.input_username().send_keys(valid_phone)
    auth_elements.input_password().click()
    assert auth_tab_active.check_tab_phone() == "Телефон"


<<<<<<< HEAD
def test_auth_login_auto_change_tab_from_email(browser, auth_elements, auth_tab, auth_tab_active):
=======
def test_auth_login_auto_change_tab_from_email(auth_elements, auth_tab, auth_tab_active):
>>>>>>> 9e2064e (Initial commit)
    """Проверка автоматической смены таба выбора аутентификации при вводе логина из вкладки Почта"""

    auth_elements.go_to_site()
    auth_tab.click_tab_email()
    auth_elements.input_username().send_keys(valid_login)
    auth_elements.input_password().click()
    assert auth_tab_active.check_tab_login() == "Логин"


<<<<<<< HEAD
def test_auth_ls_auto_change_tab_from_email(browser, auth_elements, auth_tab, auth_tab_active):
=======
def test_auth_ls_auto_change_tab_from_email(auth_elements, auth_tab, auth_tab_active):
>>>>>>> 9e2064e (Initial commit)
    """Проверка автоматической смены таба выбора аутентификации при вводе лицевого счёта из вкладки Почта"""

    auth_elements.go_to_site()
    auth_tab.click_tab_email()
    auth_elements.input_username().send_keys(valid_ls)
    auth_elements.input_password().click()
    assert auth_tab_active.check_tab_ls() == "Лицевой счёт"


<<<<<<< HEAD
def test_auth_phone_auto_change_tab_from_login(browser, auth_elements, auth_tab, auth_tab_active):
=======
def test_auth_phone_auto_change_tab_from_login(auth_elements, auth_tab, auth_tab_active):
>>>>>>> 9e2064e (Initial commit)
    """Проверка автоматической смены таба выбора аутентификации при вводе номера телефона из вкладки Логин"""

    auth_elements.go_to_site()
    auth_tab.click_tab_login()
    auth_elements.input_username().send_keys(valid_phone)
    auth_elements.input_password().click()
    assert auth_tab_active.check_tab_phone() == "Телефон"


<<<<<<< HEAD
def test_auth_email_auto_change_tab_from_login(browser, auth_elements, auth_tab, auth_tab_active):
=======
def test_auth_email_auto_change_tab_from_login(auth_elements, auth_tab, auth_tab_active):
>>>>>>> 9e2064e (Initial commit)
    """Проверка автоматической смены таба выбора аутентификации при вводе электронной почты из вкладки Логин"""

    auth_elements.go_to_site()
    auth_tab.click_tab_login()
    auth_elements.input_username().send_keys(valid_email)
    auth_elements.input_password().click()
    assert auth_tab_active.check_tab_email() == "Почта"


<<<<<<< HEAD
def test_auth_ls_auto_change_tab_from_login(browser, auth_elements, auth_tab, auth_tab_active):
=======
def test_auth_ls_auto_change_tab_from_login(auth_elements, auth_tab, auth_tab_active):
>>>>>>> 9e2064e (Initial commit)
    """Проверка автоматической смены таба выбора аутентификации при вводе лицевого счёта из вкладки Логин"""

    auth_elements.go_to_site()
    auth_tab.click_tab_login()
    auth_elements.input_username().send_keys(valid_ls)
    auth_elements.input_password().click()
    assert auth_tab_active.check_tab_ls() == "Лицевой счёт"


<<<<<<< HEAD
def test_auth_phone_auto_change_tab_from_ls(browser, auth_elements, auth_tab, auth_tab_active):
=======
def test_auth_phone_auto_change_tab_from_ls(auth_elements, auth_tab, auth_tab_active):
>>>>>>> 9e2064e (Initial commit)
    """Проверка автоматической смены таба выбора аутентификации при вводе номера телефона из вкладки Лицевой счёт"""

    auth_elements.go_to_site()
    auth_tab.click_tab_ls()
    auth_elements.input_username().send_keys(valid_phone)
    auth_elements.input_password().click()
    assert auth_tab_active.check_tab_phone() == "Телефон"


<<<<<<< HEAD
def test_auth_email_auto_change_tab_from_ls(browser, auth_elements, auth_tab, auth_tab_active):
=======
def test_auth_email_auto_change_tab_from_ls(auth_elements, auth_tab, auth_tab_active):
>>>>>>> 9e2064e (Initial commit)
    """Проверка автоматической смены таба выбора аутентификации при вводе электронной почты из вкладки Лицевой счёт"""

    auth_elements.go_to_site()
    auth_tab.click_tab_ls()
    auth_elements.input_username().send_keys(valid_email)
    auth_elements.input_password().click()
    assert auth_tab_active.check_tab_email() == "Почта"


<<<<<<< HEAD
def test_auth_login_auto_change_tab_from_ls(browser, auth_elements, auth_tab, auth_tab_active):
=======
def test_auth_login_auto_change_tab_from_ls(auth_elements, auth_tab, auth_tab_active):
>>>>>>> 9e2064e (Initial commit)
    """Проверка автоматической смены таба выбора аутентификации при вводе логина из вкладки Лицевой счёт"""

    auth_elements.go_to_site()
    auth_tab.click_tab_ls()
    auth_elements.input_username().send_keys(valid_login)
    auth_elements.input_password().click()
    assert auth_tab_active.check_tab_login() == "Логин"
<<<<<<< HEAD
=======


>>>>>>> 9e2064e (Initial commit)
