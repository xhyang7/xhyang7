#!/usr/bin/python3
import pymysql

class get_db_con():
    # 打开数据库连接
    # def get_connect(self):
    db = pymysql.connect(host='127.0.0.1',
                         port=4001,
                         user='root',
                         password='mop@123',
                         database='xhyang7',
                         charset = 'utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # sql 语句
    sql=""

    #sql 查询语句
    sql_sel_all = "SELECT * FROM students ;"

    #print
    def get_all_student_info(cursor,sql):
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(type(results))
        # print(type(results[1][4]))
        for row in results:
            id = row[0]
            name = row[1]
            stu_class=row[2]
            stu_class_num=row[3]
            stu_age=row[4]
            subject_yw=row[5]
            subject_sx=row[6]
            subject_wy=row[7]
            gross_score=subject_yw+subject_sx+subject_wy
            print("id:%d" % id,"姓名:%s" % name,stu_class,"%s班" % stu_class_num,"%d岁" % stu_age,"语文:%d" % subject_yw,"数学:%d" % subject_sx,"外语:%d" % subject_wy,"总分:%d" % gross_score)

    #DB_INFO
    def echo_db_info(cursor):
        #
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 获取数据.
        data = cursor.fetchone()
        # print(type(data[0]))
        print("Database version : %s " % data)

    def close_connect(db):
        # print("db close")
        db.close()

    def highest_score(cursor,sql):
        cursor.execute(sql)
        results = cursor.fetchall()
        highest_score=0
        whos_id=results[0]
        for row in results:
            gross_score = row[5]+row[6]+row[7]
            if gross_score > highest_score:
                highest_score = gross_score
                whos_id=row
        # print("所有学生中最高分为：%d" % highest_score)
        return whos_id
    #function demo
    #get_all_student_info(cursor,sql_sel_all)
    #echo_db_info(cursor)
    # highest_score(cursor,sql_sel_all)

    # 关闭数据库连接
    #close_connect(db)