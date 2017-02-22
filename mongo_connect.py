import pymongo

# 建立连接
client = pymongo.MongoClient('127.0.0.1', 27017)

# 创建数据库
db = client.douban

# 插入
# for i in range(10):
#     db.my_collection.insert_one({'b': i})
# for i in range(10):
#     db.movie.insert_one({'b': i})

# 更新多条记录要使用$inc
results = db.movie.find({'评分': {'$gt': '9.4'}})
text = '-'
item = map(lambda a:a['电影名'],results)
print(text.join(item))
# 查找a小于5，或者b大于等于2的记录


