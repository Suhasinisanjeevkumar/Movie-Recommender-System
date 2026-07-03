import requests

url = "https://api.themoviedb.org/3/movie/19995?api_key=801a12ecaa6eadc88f795a9ff0a5ad64&language=en-US"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=15)

print(response.status_code)
print(response.text[:300])