import requests
import random
import string
import constants as cnst


# метод создания нового пользователя - возвращает список данных о пользователе
# если регистрация не удалась, возвращает пустой список
def create_new_user():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    email_pass_name_at = []

    # генерируем логин, пароль и имя пользователя
    email = generate_random_string(8) + '@ya.ru'
    password = generate_random_string(8)
    name = generate_random_string(8)

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post(cnst.URL + cnst.API_USER_REG, data=payload)

    # если регистрация прошла успешно (код ответа 200), добавляем в список данные о пользователе
    if response.status_code == 200:
        email_pass_name_at.append(email)
        email_pass_name_at.append(password)
        email_pass_name_at.append(name)
        email_pass_name_at.append(response.json()["accessToken"])

    # возвращаем список
    return email_pass_name_at


# метод удаляет пользователя
def delete_user(token):
    requests.delete(cnst.URL + cnst.API_USER_AUTH, headers={'Authorization': token})
