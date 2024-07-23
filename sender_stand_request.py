import configuration
import requests
import data
def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
    headers=data.headers,
    json=products_ids)
response = post_products_kits(data.product_ids)


print(response.status_code)
print(response.json())
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
response = post_new_user(data.user_body);

# Вывод HTTP-статус кода ответа на запрос
# Код состояния указывает на результат обработки запроса сервером
print(response.status_code)

# Функция response.json() позволяет получить тело ответа в формате JSON.
# Это полезно для извлечения данных, полученных в результате запроса,
# особенно когда сервер возвращает полезные данные в формате JSON.
# Здесь мы вызываем эту функцию и выводим полученный JSON в консоль для наглядности.
print(response.json())
def get_users_table():
    # Составление полного URL пути к данным таблицы пользователей
    # путем конкатенации базового URL сервиса и конечной точки таблицы пользователей
    # Возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# Выполнение функции и сохранение ответа в переменную response
response = get_users_table()

# Вывод статус-кода ответа сервера в консоль
# Статус-коды HTTP сообщают о результате выполнения запроса
print(response.status_code)