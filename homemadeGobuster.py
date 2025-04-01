import requests

urlHack = open('urlPath.txt', 'r') # Word list is placed here.
baseUrl = 'https://example.org/' # Add the target URL here.
response = requests.get(baseUrl)

for line in urlHack:
    response = requests.get(baseUrl + line.strip())
    print(str(response) + " " + line.strip())

urlHack.close()

#Output:
#<Response [200]> index.html
#<Response [404]> about
#<Response [404]> contact
#<Response [404]> blog
#<Response [404]> login
#<Response [404]> register
#<Response [404]> dashboard
#<Response [404]> products
#<Response [404]> privacy-policy
#<Response [404]> terms-of-service
