'''
Real-world Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web screaping often involves making numerous network requests to
fetch web pages. These tasks are I/O-bound because they spend a lot of
time waiting for responses from server. Multithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently.
'''

import threading 
import requests
from bs4 import BeautifulSoup

urls=[
"https://python.langchain.com/docs/introduction/",
"https://python.langchain.com/docs/concepts/",
"https://python.langchain.com/docs/tutorials/"
]


def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content, 'html.parser')
    print(f'Fetch {(len(soup.text))} characters from {url}')

threads = []

for url in urls:
    thread=threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")

