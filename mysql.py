"""
    @author:wudong
    @software:PyCharm
    @file:mysql.py
    @time:2020/2/26 下午3:12
    @desc: pymysql 基本操作流程
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


# 关闭游标和数据库连接
cur.close()
db.close()
