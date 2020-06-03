from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

#news from Daily Mirror

toi_r = requests.get("http://www.dailymirror.lk/latest-news/108")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')

toi_headings = toi_soup.find_all('h3')

toi_headings = toi_headings[0:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



#news from Sunday Observer

ht_r = requests.get("http://www.sundayobserver.lk/news")
ht_soup = BeautifulSoup(ht_r.content, 'html.parser')
ht_headings = ht_soup.findAll("div", {"class": "content"})
ht_headings = ht_headings[2:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)


def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'ht_news': ht_news})