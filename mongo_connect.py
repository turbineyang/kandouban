import pymongo

# 建立连接
client = pymongo.MongoClient('127.0.0.1', 27017)

# 创建数据库
db = client.test

# 插入
for i in range(10):
    db.my_collection.insert_one({'b': i})
for i in range(10):
    db.movie.insert_one({'b': i})

# 更新多条记录要使用$inc
db.movie.update_many({'a': 2}, {'$inc': {'x': 3, 'g': 9}})

# 查找a小于5，或者b大于等于2的记录
for i in db.movie.find({'$or': [{'a': {'$lt': 5}}, {'b': {'$gte': 2}}]}):
    print(i)

mydb = client.kandouban

data = {'name': 'yagger',
        'age': '25',
        'sex': 'male'}
mydb.movie.insert(data)
