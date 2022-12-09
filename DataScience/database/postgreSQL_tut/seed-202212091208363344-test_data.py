from utils import DBManipulation

dbObj = DBManipulation()


dbObj.insert_data(
    "product", {"name": "adams", "price": 2000, "qty": 2, "category": "tanagholat"})
