import requests

URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

responce = requests.get(URL)

FILENAME = 'data.txt'

with open(FILENAME, 'w') as f:
    f.writelines(responce.text)

def parse_log(file):
    temp = []
    result = []
    if file:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                ip = line.split(" - - ")[0]
                rsp_and_pth = line.split('"')[1]
                rsp = rsp_and_pth.split()[0]
                pth = rsp_and_pth.split()[1]
                temp.append(ip)
                temp.append(rsp)
                temp.append(pth)
                result.append(tuple(temp))
                temp = []
            print(result)

parse_log('data.txt')
