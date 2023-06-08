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


def generate_random_chinese(length):
    characters = '张许李满智飞宇美励德'
    return ''.join(random.choice(characters) for _ in range(length))

# 生成随机日期
def generate_random_date(start_date, end_date):
    days = (end_date - start_date).days
    random_days = random.randint(0, days)
    return start_date + datetime.timedelta(days=random_days)

# 插入1000条数据
for _ in range(1000):
    expected_date = generate_random_date(datetime.datetime(2022, 1, 1), datetime.datetime(2023, 5, 31))
    exact_date = generate_random_date(datetime.datetime(2022, 1, 1), datetime.datetime(2023, 5, 31))
    receiver_name = generate_random_chinese(3)
    sender_id = random.randint(102, 251)
    package_type = random.choice(['危险品', '国际快递', '普通国内快递'])
    # 执行插入语句
    insert_query = "INSERT INTO Package (ExceptedDate, ExactDate, ReceiverName, SenderID, type) VALUES (%s, %s, %s, %s, %s)"
    values = (expected_date, exact_date, receiver_name, sender_id, package_type)
    cursor.execute(insert_query, values)

# 提交事务并关闭连接
conn.commit()
conn.close()
