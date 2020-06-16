import pymysql
import random

def yield_random_missile(i):
    id = "L{:02}B".format(i)

    x = 88.418075+random.random()*(88.629643-88.418075)
    y = 28.865215+random.random()*(28.958678-28.865215)
    h = 2000*random.random()

    speed = 30+random.random()*20
    direct = 360*random.random()-180
    distance = random.random()*50

    return {'identity':id, 'x':x, 'y':y, 'h':h, 's':speed, 'dir':direct, 'dis':distance}

def yield_random_droneData(i):
    id = "L{:02}A".format(i)

    x = 88.418075+random.random()*(88.629643-88.418075)
    y = 28.865215+random.random()*(28.958678-28.865215)
    h = 2000*random.random()

    speed = 30+random.random()*20
    direct = 360*random.random()-180
    distance = random.random()*50

    return {'identity':id, 'x':x, 'y':y, 'h':h, 's':speed, 'dir':direct, 'dis':distance}

def yield_random_vehicleData(i):
    id = "L{:02}C".format(i)

    x = 88.418075+random.random()*(88.629643-88.418075)
    y = 28.865215+random.random()*(28.958678-28.865215)
    h = 2000*random.random()

    speed = 30+random.random()*20
    direct = 360*random.random()-180
    distance = random.random()*50

    return {'identity':id, 'x':x, 'y':y, 'h':h, 's':speed, 'dir':direct, 'dis':distance}


def main():
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='root',
                           db='subprime',
                           charset='utf8')

    cur = conn.cursor()

    # 插入12条巡飞弹的记录
    for i in range(12):
        data = yield_random_missile(i+1)
        print(data)
        query = """
        insert into missile values(
            '{identity}',
            {x},
            {y},
            {h:.2f},
            {s:.2f},
            {dir:.2f},
            {dis:.2f}
        )
        """.format(identity=data['identity'],
                   x=data['x'],
                   y=data['y'],
                   h=data['h'],
                   s=data['s'],
                   dir=data['dir'],
                   dis=data['dis'])
        cur.execute(query)
        conn.commit()

    # 插入6个无人机的记录
    for i in range(6):
        data = yield_random_droneData(i+1)
        query = '''
        insert into drones values(
            '{id}',
            {longitude},
            {latitude},
            {height},
            {speed},
            {direction},
            {distance}
        )
        '''.format(id=data['identity'],
                   longitude=data['x'],
                   latitude=data['y'],
                   height=data['h'],
                   speed=data['s'],
                   direction=data['dir'],
                   distance=data['dis'])
        cur.execute(query)
        conn.commit()

    # 插入2个无人车的记录
    for i in range(2):
        data = yield_random_vehicleData(i+1)
        query = '''
        insert into vehicle values(
            '{id}',
            {longitude},
            {latitude},
            {height},
            {speed},
            {direction},
            {distance}
        )
        '''.format(id=data['identity'],
                   longitude=data['x'],
                   latitude=data['y'],
                   height=data['h'],
                   speed=data['s'],
                   direction=data['dir'],
                   distance=data['dis'])
        cur.execute(query)
        conn.commit()

    conn.close()



if __name__=='__main__':
    main()