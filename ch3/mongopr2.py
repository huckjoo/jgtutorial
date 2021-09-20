from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.dbjungle

# 매트릭스 평점 가져오기
# mat = db.movies.find_one({"title": "매트릭스"})

# 매트릭스의 평점과 같은 평점의 영화 제목들을 가져오기
# titles = list(db.movies.find({"star": mat["star"]}))
# (주의!) list화 하지 않으면 object로 불러와진다.

# 매트릭스 평점을 0으로 만들어버리기
db.movies.update_one({"title": "매트릭스"}, {"$set": {"star": 0}})
mat = db.movies.find_one({"title": "매트릭스"})
print(mat["star"])
