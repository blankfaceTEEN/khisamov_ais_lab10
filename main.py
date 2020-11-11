import requests
from bs4 import BeautifulSoup


def get_response(url, head):
    return requests.get(url, headers=head)


def parse():
    results = []
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        page = 1
        for element in soup.find_all('div', class_='yuRUbf'):
            anchors = element.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = element.find('h3', class_='LC20lb DKV0Md').text
                item = {
                    "page": page,
                    "url": link,
                    "title": title
                }
                page += 1
                results.append(item)
    else:
        print(resp.status_code)
    return results


def output(results):
    print(results[0])
    print(results[1])


headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}
query = input("Введите ваш запрос: ")
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"
resp = get_response(URL, headers)
output(parse())
