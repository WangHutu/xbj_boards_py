import pymongo
import uuid
myclient = pymongo.MongoClient('mongodb://localhost:27017')

def verify_db(db, collection):
    list = myclient.list_database_names()
    if not list or db not in list:
        newdb = myclient[db]
        collection = newdb[collection]
        

# 插入数据
def insertDbData(db, collection, data, verifyData='', attr=''):
    verify_db(db, collection)
    s = False
    if verifyData:
        verify = getDbData(db, collection, verifyData)
        datas = list(verify)
        for item in datas:
            s = item.get(attr)
    if (not s):
        print(data, 'data')
        data.update({"id": str(uuid.uuid1())})
        print(data, 'data')
        myclient[db][collection].insert_one(data) 
    return not s
    
# 查询数据
def getDbData(db, collection, data):
    if (data):
        print('数据库查出的数据1', myclient[db].get_collection(collection).find(data))
        return myclient[db].get_collection(collection).find(data)
    else:
        print('数据库查出的数据2', myclient[db][collection].find())
        return myclient[db][collection].find()
    

# 更新数据
def updateDbData(db, collection, data, serchData):
    myclient[db][collection].update_one(serchData, {"$set":data})
    return True


# 删除数据
def delDbData(db, collection, data):
    myclient[db][collection].delete_one(data)
    return True
