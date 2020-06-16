# 连接mysql

```
import pymysql
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='root',
                       db='uavs',
                       charset='utf8')

curs = conn.cursor()  # 游标用来执行sql语句和返回查询返回值
```

# 执行sql语句 返回查询结果

```buildoutcfg
    
    conn.execute('''
    sql语句 （创建、查询、修改数据）
    ''')
    # 抓取查询结果
    curs.fetchall()
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()
```
