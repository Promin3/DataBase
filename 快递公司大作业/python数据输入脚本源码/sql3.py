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


# 插入1000条数据
for _ in range(1000):
    payment_date = generate_random_date(datetime.datetime(2022, 1, 1), datetime.datetime(2023, 5, 31))
    amount = round(random.uniform(10, 50), 2)

    # 从Package表中随机选择一条记录
    cursor.execute("SELECT SenderID, PackageID FROM Package ORDER BY RAND() LIMIT 1")
    result = cursor.fetchone()
    sender_id = result[0]
    package_id = result[1]

    # 执行插入语句
    insert_query = "INSERT INTO Receipt (PaymentDate, amount, CustomerID, PackageID) VALUES (%s, %s, %s, %s)"
    values = (payment_date, amount, sender_id, package_id)
    cursor.execute(insert_query, values)

# 提交事务并关闭连接
conn.commit()
conn.close()
