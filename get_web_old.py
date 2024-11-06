import requests

res = requests.get('https://google.com')

if res.status_code == 200:
    print(res)
    print(res.text)
    out_file = open('google.html', 'w', encoding='utf8')
    out_file.write(res.text)
    out_file.close()
else:
    print('Error:', res.status_code)