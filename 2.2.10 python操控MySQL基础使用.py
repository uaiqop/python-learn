from pymysql import Connection

# 构建到数据库的连接
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="973610"
)

print(conn.get_server_info())

# 关闭连接
conn.close()
