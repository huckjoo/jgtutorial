import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
data = requests.get(
    "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20200303"
)
# soup에는 페이지의 모든 정보들이 담겨있다.
soup = BeautifulSoup(data.text, "html.parser")
# select를 사용해서 movies만 가져오자.
movies = soup.select("#old_content > table > tbody > tr")
for movie in movies:
    stars = movie.select_one("td.point")
    a_tag = movie.select_one("td.title > div > a")
    rank = movie.select_one("td.ac > img")
    if stars is not None and a_tag is not None and rank is not None:
        print(rank["alt"], a_tag.text, stars.text)
