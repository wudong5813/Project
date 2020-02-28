"""
    @author:wudong
    @software:PyCharm
    @file:read_db2.py
    @time:2020/2/26 下午3:41
    @desc:
"""
import pymysql

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="student",
                     charset="utf8");

# 创建游标 (操作数据 执行sql语句,获取结果)
cur = db.cursor();

# 输入一个名字查看他的信息:
# name = input("Name:")
# sql = 'select * from cls where name = "%s";'%name
# cur.execute(sql)
# print(cur.fetchall())

# 输入一个名字查看他的信息:
name = input("Name:")
sql = "select * from cls where name = %s or score > %s;"
cur.execute(sql,[name,90]) # 值传递数据参量,不传递关键字,表明,数据库名,字段名等
print(cur.fetchall())

# 关闭游标和数据库连接
cur.close()
db.close()
