

import requests
# Создание вызова API и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

# Сохранение ответа API в переменной.
response_dict = r.json()

# Обработка результатов.
print(response_dict.keys())
print('Total repositories: ' + str(response_dict['total_count']))

# Анализ информации о репозиториях.
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))
print("\nSelected information about each repository:")
for repo_dict in repo_dicts[0:5]:
    print('\nName:', repo_dict['name'])
    print('Stars:', repo_dict['stargazers_count'])
