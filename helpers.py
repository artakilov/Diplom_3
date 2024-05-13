import allure
import requests
import random
import string
import constants as cnst
import data_for_tests as dft


@allure.step('Генерируем строку, состоящую только из букв нижнего регистра длиной {length}')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Создаем нового пользователя, возвращаем данные о новом пользователе')
def create_user():
    new_user = {}
    email = generate_random_string(8) + '@ya.ru'
    password = generate_random_string(8)
    name = generate_random_string(8)
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(cnst.URL + cnst.API_USER_REG, data=payload)
    if response.status_code == 200:
        new_user = {
            "email": email,
            "password": password,
            "name": name,
            "response": response
        }
    return new_user


@allure.step('Удаляем пользователя')
def delete_user(token):
    requests.delete(cnst.URL + cnst.API_USER_AUTH, headers={'Authorization': token})


@allure.step('Создаем заказ')
def create_order(token):
    response = requests.post(cnst.URL + cnst.API_ORDER, data=dft.with_ingredient, headers={'Authorization': token})
    return response.json()["order"]["number"]
