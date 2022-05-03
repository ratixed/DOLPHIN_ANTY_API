import requests

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Authorization': 'Bearer null',
    'User-Agent': 'dolphin_anty_2022.117.1_Darwin',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Referer': 'http://anty-frontend.dolphin.ru.com/',
    'Accept-Language': 'ru',
}

json_data = {
    'username': '<your_login>',  # Replace <your_login> to your login for Dolphin Anty Browser
    'password': '<your_password',  # Replace <your_password> to your login for Dolphin Anty Browser
}

response = requests.post('http://142.132.182.77:81/auth/login', headers=headers, json=json_data, verify=False)

print(response.json()['token'])
