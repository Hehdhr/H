
import requests

def search_unused_usernames():
    base_url = "https://api.tiktok.com/"
    params = {
        "method": "user.search",
        "count": 100,
        "keyword": "zzzz", # تغيير #### بالحروف التي تريد البحث عنها
        "retry_times": 5
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    usernames = []

    if data["statusCode"] == 0:
        for user in data["userList"]:
            usernames.append(user["nickname"])

    return usernames

unused_usernames = search_unused_usernames()
print(unused_usernames)
