import psycopg2
import psycopg2.extras
import pandas as pd


# SELECT col1,.... FROM table_name;   ||||| SELECT * FROM table_name;


# Connect to your postgres DB
conn = psycopg2.connect(
    host="localhost",
    database="ml",
    user="mapsa",
    password="mapsa1234")

# pandas dataframe
# df = pd.read_sql_query("SELECT * FROM users", conn)

# Open a cursor to perform database operations
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
# cur = conn.cursor()


# find users
cur.execute("SELECT username FROM users")
# print(cur.description)

# query = "SELECT * FROM users"
# query = "SELECT * FROM users WHERE username LIKE 'A%' OR age BETWEEN 10 AND 18"
# query = "SELECT * FROM users ORDER BY age DESC"
# query = "SELECT * FROM users WHERE age IS NULL ORDER BY age"
# query = "UPDATE users SET age=50 WHERE username='Ashkan'"
# query = "DELETE FROM users WHERE username='Ashkan'"
# query = "SELECT MIN(age) AS min_age FROM users"
# query = "SELECT COUNT(*) FROM users"
# query = "SELECT AVG(age) FROM users"
# query = """
#             SELECT name, price, cartItem.qty AS kharid_qty ,product.qty AS mojudi
#                     FROM cartItem
#                     INNER JOIN product
#                     ON cartItem.product_id=product.product_id
#         """

query = """ 
            SELECT category, AVG(price) 
                    FROM product 
                    GROUP BY category
        """


cur.execute(query)
# conn.commit()

# Retrieve query results
records = cur.fetchall()

# print(records)
print([dict(record) for record in records])

# # print("users: \n", [record["username"] for record in records])

# ########################## aggregation
# # average price product

# cur.execute("SELECT category, avg(price) AS price_ave, sum(price) as sum_products FROM product WHERE name LIKE 'p%' GROUP BY category")
# result = cur.fetchall()
# # print([dict(res) for res in result])

# cur.execute("SELECT product.name AS product_name, cartItem.qty AS tedad, (SELECT username FROM myuser WHERE user_id=cart.user_id) AS username FROM cartItem JOIN product ON cartItem.product_id=product.product_id JOIN cart ON cartItem.cart_id = cart.cart_id")
# result = cur.fetchall()
# print([dict(res) for res in result])
