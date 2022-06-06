
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

info_songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for song in info_songs:
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    rank = song.select_one('td.number').text[0:2]
    singer = song.select_one('td.info > a.artist.ellipsis').text
    print(rank, title, singer)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
# print(movies['title']) >> 태그의 속성을 알고싶으면 태그['속성']
# print(movies.text) >> 태그 안에 텍스트를 보고싶으면 태그.text


