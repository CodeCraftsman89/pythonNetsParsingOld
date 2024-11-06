import requests

url = 'https://habr.com/ru/search'

headers = {"Accept": "text/html,application/xhtml+xml,"
                     "application/xml,q=0.9,image/avif,image/webp,image/apng,"
                     "*/*,q=0.8application/signed-exchange:v=b3:q=0.7",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                         "AppleWebKit/537.36 (KHTML, like Gecko)"
                         "Chrome/83.0.4103.116 Safari/537.36"
           }


query = {"q": "html css"}

res = requests.get(url, headers=headers, params=query)
if res.status_code == 200:
    print(res)
    print(res.text)
    out_file = open('habr.html', "w", encoding='utf-8')
    out_file.write(res.text)
    out_file.close()
else:
    print("Error")
