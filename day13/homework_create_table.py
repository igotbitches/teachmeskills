import psycopg2

conection = psycopg2.connect(
  database="product",
  user="postgres",
  password="postgres",
  host="127.0.0.1",
  port="5432"
)
print("Database opened successfully")

cur = conection.cursor()
cur.execute("""CREATE TABLE shop_product  
     (id serial primary key,
     name varchar ,
     price integer,
     amount integer ,
     comment varchar );""")

print("Table created successfully")
conection.commit()
conection.close()

