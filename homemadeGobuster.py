import requests
import sys
#{ user@machine:~$ python3 homemadeGobuster.py url list.txt }
# Accepts arguments at terminal execution in the above format. Make sure to include a forward slash
# at the end of the url depending on the list.

urlHack = open(sys.argv[2], 'r')#open('urlPath.txt', 'r')
baseUrl = sys.argv[1]#'https://example.org/'
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
