#!/usr/bin/python3
import pymysql_get_con
db=pymysql_get_con.get_db_con.db
cursor = db.cursor()

new_class=pymysql_get_con.get_db_con

#get all students info
sql=new_class.sql_sel_all
new_class.get_all_student_info(cursor,sql)

while(True):
    chose_class=input("请输入需要查询的年级（如：一年级）：")
    if chose_class == "一年级":
        break
    elif chose_class == "二年级":
        break
    elif chose_class == "三年级":
        break
    else:
        print("输入有误，请重新输入需要查询的年级")

# 查询 X 年级学生最高分 及 学生信息
def get_class_top_score(chose_class):
    class_sql="select * from students where class = \""+chose_class+"\";"
    # print(class_sql)
    class_1_score=new_class.highest_score(cursor,class_sql)
    # print(class_1_score)
    class_2_score=class_1_score[5]+class_1_score[6]+class_1_score[7]
    print("%s" % chose_class +"中最高分为：%d" % class_2_score,"学生姓名为：%s" % class_1_score[1],"班级为：%d班" % class_1_score[3])
get_class_top_score(chose_class)

#close db connect
pymysql_get_con.get_db_con.close_connect