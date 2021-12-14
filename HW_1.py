import requests
import time
import json

def get_data(url: str) -> dict:
    while True:
        time.sleep(1)
        response = requests.get(url)
        if response.status_code == 200:
            break
    return response.json()

username = input('Введите username: ')
username = 'Berezhnyak4' if username == '' else username
url = 'https://api.github.com/users/'+username+'/repos'

response = get_data(url)
print('Получен результат')
print(response)

repo = []
for itm in response:
    repo.append(itm['name'])
print(f'Список репозиториев пользователя {username}')
print(repo)

with open('1_1_repo.json', 'w') as f:
    json_repo = json.dump(repo, f)