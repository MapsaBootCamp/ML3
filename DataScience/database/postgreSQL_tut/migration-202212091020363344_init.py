from utils import DBManipulation

dbObj = DBManipulation()
dbObj.create_table("users", """
                        user_id serial PRIMARY KEY,
                        username VARCHAR(50) UNIQUE NOT NULL,
                        age INT CHECK(age > 0)
                    """
                   )

dbObj.create_table("product", """
                product_id serial PRIMARY KEY, 
                name VARCHAR ( 50 ) UNIQUE NOT NULL, 
                price INT CHECK(price > 0),
                qty INT CHECK(qty >= 0),
                category VARCHAR(20) NOT NULL
            """
                   )

dbObj.create_table("cart", """
                cart_id serial PRIMARY KEY,
                user_id INT NOT NULL REFERENCES users ON DELETE CASCADE,
                FOREIGN KEY (user_id)
                    REFERENCES users (user_id)
            """
                   )


dbObj.create_table("cartItem", """
                id serial PRIMARY KEY, 
                cart_id INT NOT NULL REFERENCES cart ON DELETE CASCADE, 
                product_id INT NOT NULL,
                qty INT CHECK(qty >= 0), 
                FOREIGN KEY (cart_id) 
                    REFERENCES cart (cart_id),
                FOREIGN KEY (product_id) 
                    REFERENCES product (product_id)
            """
                   )
