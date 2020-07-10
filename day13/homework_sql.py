import psycopg2
import pprint

while True:
    sign = input("Какие действия вам необходимо совершить? \n"
        "create, read, update, delete, stop: ")
    if sign in ('create', 'read', 'update', 'delete', 'stop'):
        connection = psycopg2.connect(
            database="product",
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port="5432")
        if sign == 'stop':
            connection.close()
            break
        if sign == 'create':
            a_name = str(input('name: '))
            a_price = int(input("price: "))
            a_amount = int(input("amount: "))
            a_comment = str(input("comment: "))
            cur = connection.cursor()
            cur.execute(f"INSERT INTO shop_product (name, price, amount, comment) "
                        f"values ('{a_name}', {a_price}, {a_amount}, '{a_comment}')")
            connection.commit()
        if sign == 'read':
            cur = connection.cursor()
            cur.execute("SELECT * FROM shop_product")
            result = cur.fetchall()
            pprint.pprint(result)
        if sign == 'delete':
            x = int(input('id: '))
            cur = connection.cursor()
            cur.execute(f"DELETE FROM shop_product WHERE id={x}")
            connection.commit()
        if sign == 'update':
            change = input('Что нужно изменить?\nname, price, amount, comment: ')
            if change in ('name', 'price', 'amount', 'comment'):
                if change == 'name':
                    u_name = str(input("name: "))
                    x = int(input('id: '))
                    cur = connection.cursor()
                    cur.execute(f"UPDATE shop_product SET name='{u_name}' WHERE id={x}")
                    connection.commit()
                if change == 'price':
                    u_price = str(input("price: "))
                    x = int(input('id: '))
                    cur = connection.cursor()
                    cur.execute(f"UPDATE shop_product SET price={u_price} WHERE id={x}")
                    connection.commit()
                if change == 'amount':
                    u_amount = int(input("amount: "))
                    x = int(input('id: '))
                    cur = connection.cursor()
                    cur.execute(f"UPDATE shop_product SET amount={u_amount} WHERE id={x}")
                    connection.commit()
                if change == 'comment':
                    u_comment = str(input("comment: "))
                    x = int(input('id: '))
                    cur = connection.cursor()
                    cur.execute(f"UPDATE shop_product SET comment='{u_comment}' WHERE id={x}")
                    connection.commit()