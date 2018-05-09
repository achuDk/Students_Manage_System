import pymysql


HOST = "localhost"
PORT = 3306
USER = "root"
PASSWD = "123456"
DB = "django_demo_sys"

conn = pymysql.connect(host=HOST,port=PORT,user=USER,passwd=PASSWD,db=DB)
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


def sql_exe(sql):
    print('===========>',sql)
    cursor.execute(sql)
    row_all = cursor.fetchall()

    print("执行结果：")
    print(row_all)
    # for i in row_all:
    #     for j, k in i.items():
    #         print(j, ':', k)
    print("[执行结果行数] ：", len(row_all))
    conn.commit()

    return row_all
