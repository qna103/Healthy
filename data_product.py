import pymongo

client = pymongo.MongoClient("mongodb+srv://homlessss:4BQoyCkal5qV7r6r@cluster0-yzgzn.mongodb.net/test?retryWrites=true")
db = client.data_product

# Tìm kiếm các sản phẩm có tên được nhập vào
def find_product(name):
    return list(db.data.find({'name' : name}))

# Cập nhật giá của sản phẩm có tên được nhập vào
def update_product(name, price):
    db.data.update_one({'name' : name},{"$set":{"price" : price}})

# Xóa mặt hàng được truyền vào
def delete(name):
    db.data.delete_one({'name' : name})

# Hàm thêm sản phẩm
def add_product(name, price, img_url):
    db.data.insert_one({'name' : name, 'price' : price, 'img_url' : img_url})

db.data.insert_one({'name' : 'Genius Joy', 'price' : '59.99$' , 'img_url' : '/static/images/Brain-Bot.png'})
db.data.insert_one({'name' : 'Genius Consciousness', 'price' : '37.99$', 'img_url' : '/static/images/Brain-Bot.png'})
db.data.insert_one({'name' : 'Genius Muscle Builder', 'price' : '89.99$', 'img_url' : '/static/images/Brain-Bot.png'})
