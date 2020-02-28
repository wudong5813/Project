"""
    @author:wudong
    @software:PyCharm
    @file:read_db.py
    @time:2020/2/26 下午3:23
    @desc:数据库查询操作
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

# 执行各种数据操作
sql = "select name,age,score from cls where score > 90;"
cur.execute(sql)

# 获取结果方法1
# for i in cur:
#     print(i)

# 获取结果方法2
# print(cur.fetchone()) # 获取第一个查询结果
# print(cur.fetchall()) # 获取所有查询结果
print(cur.fetchmany(2)) # 获取2条结果

# 关闭游标和数据库连接
cur.close()
db.close()
