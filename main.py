import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=RUB&amount=100"

payload = {}
headers= {
  "apikey": "kd6L0Fya2eeMDxbG7uZToLAaDTJpCeTK"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text

print (status_code, result)