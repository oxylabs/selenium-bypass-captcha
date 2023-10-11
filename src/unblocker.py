import requests

proxy = 'http://{}:{}@unblock.oxylabs.io:60000'.format("USERNAME", "PASSWORD")

proxies = {
    'http': proxy,
    'https': proxy
}

page = "https://sandbox.oxylabs.io/products"
response = requests.get(page, proxies=proxies, verify=False)

print(response.status_code)
content = response.content
