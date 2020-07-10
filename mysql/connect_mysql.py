import pymysql
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='root',
                       db='subprime',
                       charset='utf8')

curs = conn.cursor()

def create_table():
    # 创建表
    curs.execute('''
    create table uav_state(
        id     int primary key,
        x      float,
        y      float,
        type   int
    )
    ''')

    # 从文本中读取数据，并插入表中
    query = 'insert into uav_state VALUES(%s, %s, %s, %s)'
    with open('uav_state.txt', 'r') as f:
        for line in f:
            vals = line.strip().split(" ")
            curs.execute(query, vals)  # 插入记录

    conn.commit()
    conn.close()

def state_query():

    query = 'select * from uav_state'
    curs.execute(query)
    col_names = [f[0] for f in curs.description]
    for row in curs.fetchall():
        record = ""
        for pair in zip(col_names, row):
            record += "{}:{} ".format(pair[0], pair[1])
        print(record)

if __name__=='__main__':
    state_query()