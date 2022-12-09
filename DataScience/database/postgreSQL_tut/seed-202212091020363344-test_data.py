from utils import DBManipulation

dbObj = DBManipulation()


dbObj.insert_data("users", {"username": "Ashkan", "age": 23})
dbObj.bulk_insert_data("users", [{"username": "Asghar", "age": 23}, {
    "username": "Gholam", "age": 12}])
dbObj.insert_data("product", {
                  "name": 'pofak', "price": 12000, "qty": 5, "category": 'tanagholat'})
dbObj.bulk_insert_data("product", [
    {"name": 'chips', "price": 40000, "qty": 5, "category": 'tanagholat'},
    {"name": 'panir', "price": 50000,
     "qty": 3, "category": 'mavad_ghazai'}
])
dbObj.insert_data("cart", {"user_id": 1})
dbObj.bulk_insert_data("cart", [{"user_id": 2}, {"user_id": 3}])
dbObj.bulk_insert_data("cartItem", [{"cart_id": 1, "product_id": 1, "qty": 3}, {
                       "cart_id": 1, "product_id": 2, "qty": 3}, {"cart_id": 2, "product_id": 1, "qty": 3}])
