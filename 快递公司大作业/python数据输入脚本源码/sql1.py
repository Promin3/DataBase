import random
import string
import mysql.connector  # 导入MySQL连接器模块

# 连接数据库
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='zjj2003915',
    database='expressCompany'
)

cursor = conn.cursor()

# 生成随机字符串
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def generate_random_chinese(length):
    characters = '朱张李美好天杨帅宇风飞'
    return ''.join(random.choice(characters) for _ in range(length))


# 插入50条数据
for _ in range(50):
    pay_method = random.choice(['协议支付', '支付宝', '信用卡', '微信支付'])
    name = generate_random_chinese(3)
    address = random.choice(['武汉大学街道', '华中科技大学街道', '华中师范大学街道', '武汉理工大学街道'])

    # 执行插入语句
    insert_query = "INSERT INTO Customer (payMethod, name, address) VALUES (%s, %s, %s)"
    values = (pay_method, name, address)
    cursor.execute(insert_query, values)

# 提交事务并关闭连接
conn.commit()
conn.close()
