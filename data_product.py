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

# Tìm tất cả sản phẩm cùng loại
def get_all_type(type_product):
    return list(db.data.find({'type' : type_product}))

# Hàm thêm sản phẩm
def add_product(name, price, type_product, quantity):
    db.data.insert_one({'name' : name, 'price' : price, 'type' : type_product, 'quantity': quantity})

# Cập nhật số lượng của mặt hàng, nếu số lượng = 0, xóa mặt hàng
def update_quantity():
    for i in db.data.find():
        if db.data[i]['quantity'] == 0:
            delete(db.data[i]['name']) 