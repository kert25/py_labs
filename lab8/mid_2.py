import requests


def get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        print(f"Получено {len(posts)} постов")
        for post in posts[:3]:
            print(f"  - {post['title']}")
    else:
        print(f"Ошибка: {response.status_code}")


get_posts()
