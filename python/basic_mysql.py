import mysql.connector as mydb

# コネクションの作成
conn = mydb.connect(
    host='localhost',
    port='3306',
    user='root',
    database='sakila'
)

conn.ping(reconnect=True)

print(conn.is_connected())

# DB操作用にカーソルを作成
cur = conn.cursor()

# CREATE TABLE
# cur.execute(
#     """
#     CREATE TABLE IF NOT EXISTS test_table (
#     `id` int auto_increment primary key,
#     `name` varchar(50) not null,
#     `price` int(11) not null
#     ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
#     """
# )

# SELECT
cur.execute(
     """
     CREATE TABLE IF NOT EXISTS test_table (
     `id` int auto_increment primary key,
     `name` varchar(50) not null,
     `price` int(11) not null
     ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
     """
)


