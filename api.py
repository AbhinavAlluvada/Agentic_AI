import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")
# print(response.status_code)

users = response.json()

values = users[0].copy()

# print(values["name"])

new_post = {
    "userID":101,
    "name":"Maxwell",
    "age":25,
    "country":"Austria"
}
respond = requests.post("https://jsonplaceholder.typicode.com/posts",json=new_post)

# print(respond.json())

headers = {
    "Authorization":"Maxwell_API"
}
response_v2 = requests.get("https://jsonplaceholder.typicode.com/users",headers=headers)

params = {
    "id":3
}
url_post = "https://jsonplaceholder.typicode.com/posts"
respond = requests.post(url_post,params=params)

data = {
    "id" :101,
    "name":"Arthur",
    "job":"Assassin"    
}

requests.post(url_post,json = data)

try:
    response = requests.get(url_post)
    response.raise_for_status()
    data = response.json()
    print(response.status_code)
except requests.RequestException as e:
    print(e)