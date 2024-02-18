from requests import Session
import requests
import secrets
from time import sleep
from colorama import init
from os import system

request = Session()
init(autoreset=True)
system('cls')

username = input("\n Username >>> ")
password = input("\n Username >>> ")

url = "https://fastfollow.in/member?"

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "15a9a02a93873b7832cf3274b082c714=800e48b729fa0f88fe7ce863c6d34d9a; _ga=GA1.2.920828922.1708286598; _gid=GA1.2.1090578126.1708286598",
    "Host": "fastfollow.in",
    "Origin": "https://fastfollow.in",
    "Referer": "https://fastfollow.in/member",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

payload = "username={}&password={}&userid=&antiForgeryToken={}".format(username, password, secrets.token_hex())

response = request.post(url, headers=headers, data=payload).json()

if response['status'] != "success":
    print("Failed login.")
    raise SystemExit


url = "https://fastfollow.in/ajax/keep-session"

headers = {
   "Accept": "application/json, text/javascript, */*; q=0.01",
   "Connection": "keep-alive" ,
   "Cookie": "_ga=GA1.2.920828922.1708286598; _gid=GA1.2.1090578126.1708286598; 15a9a02a93873b7832cf3274b082c714=b8feb39e3223864b3b1e4df2afd7a57a",
   "Host": "fastfollow.in",
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
   "X-Requested-With": "XMLHttpRequest"
}

response = request.get(url, headers=headers).json()

if response['status'] != "ok":
    print("Logged out, login again.")
    raise SystemExit


def userid(username: str) -> str:
    url = "https://storiesig.info/api/ig/userInfoByUsername/{}".format(username)
    response = request.get(url).json()['result']['user']['pk']
    return response

target = input("\n Target >>> ")


url = "https://fastfollow.in/tools/send-follower?formType=findUserID"

payload = "username={}".format(target)

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "_ga=GA1.2.920828922.1708286598; _gid=GA1.2.1090578126.1708286598; 15a9a02a93873b7832cf3274b082c714=dfe162848a99c8d5e75cd24fbae3a47f",
    "Host": "fastfollow.in",
    "Origin": "https://fastfollow.in",
    "Referer": "https://fastfollow.in/tools/send-follower",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

response = request.post(url, headers=headers, data=payload)

if response.status_code != 200:
    raise SystemExit

url = "https://fastfollow.in/ajax/keep-session"

headers = {
   "Accept": "application/json, text/javascript, */*; q=0.01",
   "Connection": "keep-alive" ,
   "Cookie": "_ga=GA1.2.920828922.1708286598; _gid=GA1.2.1090578126.1708286598; 15a9a02a93873b7832cf3274b082c714=b8feb39e3223864b3b1e4df2afd7a57a",
   "Host": "fastfollow.in",
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
   "X-Requested-With": "XMLHttpRequest"
}

response = request.get(url, headers=headers).json()

if response['status'] != "ok":
    print("Logged out, login again.")
    raise SystemExit

url = "https://fastfollow.in/tools/send-follower/{}?formType=send".format(userid(target))

payload = "adet=5&userID={}&userName={}".format(userid(target), target)

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "_ga=GA1.2.920828922.1708286598; _gid=GA1.2.1090578126.1708286598; 15a9a02a93873b7832cf3274b082c714=6daaba777bba5206ecfc9681320b0904",
    "Host": "fastfollow.in",
    "Origin": "https://fastfollow.in",
    "Referer": "https://fastfollow.in/tools/send-follower/{}".format(userid(target)),
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

response = request.post(url, headers=headers, data=payload).json()

if response['status'] != "success" or not response['takipKredi'] >= 0:
    print("Failed to follow! or No credits.")
    raise SystemExit

print("Followed!")
print(response)

# made by @vardxg on Telefgram!