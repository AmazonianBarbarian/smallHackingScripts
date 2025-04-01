import requests

urlHack = open('urlPath.txt', 'r')
baseUrl = 'https://example.org/'
response = requests.get(baseUrl)

for line in urlHack:
    response = requests.get(baseUrl + line.strip())
    print(str(response) + " " + line.strip())

urlHack.close()
