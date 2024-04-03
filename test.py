import requests


#token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJyb290MTIzNCIsImVtYWlsIjoidXNlckBleGFtcGxlLmNvbSIsInBob25lIjo4Nzc3MTg4ODMzMywic2Vzc2lvbl9pZCI6ImMzNjAyNmU1LTZlOWQtNDA5Zi04OWQ4LWUyMzZjOWE3ODBhYSIsInJvbGUiOjAsImV4cCI6MzkwMzY2OTU0OTV9.8SOnV7HqoJozkCNkngDxgbUBz-iB9zy7m8Aw3ETGIQA"


# Заголовок запроса с токеном JWT
#headers = {
#    "Authorization": f"Bearer {token}"
#}


# URL защищенного эндпоинта
url = "http://127.0.0.1:8000/api/v1/register"


json_data = {
    "username": "",

}



# Отправка запроса POST к защищенному эндпоинту с использованием токена JWT и отправкой JSON данных
response = requests.put(url=url)


print(response.json(), response.status_code)
