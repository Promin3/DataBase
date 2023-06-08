import random
import datetime
import mysql.connector

# 连接数据库
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='zjj2003915',
    database='expressCompany'
)

cursor = conn.cursor()


# 生成随机日期
def generate_random_date(start_date, end_date):
    days = (end_date - start_date).days
    random_days = random.randint(0, days)
    return start_date + datetime.timedelta(days=random_days)


# 从Package表中获取所有记录按顺序
cursor.execute("SELECT PackageID, ExactDate FROM Package ORDER BY PackageID")
packages = cursor.fetchall()

# 插入5000条数据
for package in packages:
    package_id = package[0]
    exact_date = package[1]

    # 插入5条数据
    for _ in range(5):
        warehouse_id = random.randint(1, 20)
        trunk_id = random.randint(1600, 1800)
        tracking_time = generate_random_date(datetime.datetime(2022, 1, 1), exact_date)

        # 执行插入语句
        insert_query = "INSERT INTO TrackingInformation (PackageID, warehouseID, TrunkID, TrackingTime) VALUES (%s, %s, %s, %s)"
        values = (package_id, warehouse_id, trunk_id, tracking_time)
        cursor.execute(insert_query, values)

# 提交事务并关闭连接
conn.commit()
conn.close()
