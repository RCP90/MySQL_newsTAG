import prettytable

# t = prettytable.PrettyTable(["id","Title"],encoding="utf8")
#
#  t.add_row(["1","AAA"])
#  t.add_row(["2","BBB"])
#  t.add_row(["3","CCC"])
#
# for i in range(1,10,1):
#     t.add_row([i,"CCC"+str(i)])
#
# t.align["id"] = "c"
# t.align["title"] = "c"
#
# print(t)

# import colorama
# colorama.init(True)
# print("ABC")
# print(colorama.Style.BRIGHT+"ABC")
# print(colorama.Fore.GREEN+"ABC")
# print(colorama.Back.RED+"ABC")
# print(colorama.Back.RED+colorama.Fore.GREEN+colorama.Style.BRIGHT+"12345")

import pymysql
link=pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    db="2020-03-31",
    charset="utf8"
)

c = link.cursor()

# title =input("請輸入標題")
# source=input("請輸入新聞")
# create_date=input("請輸入日期")
# description=input("請輸入描述")
# look=input("請輸入瀏覽率")
#
# c.execute(
#     "INSERT INTO news(title,source,create_date,description,look) " +
#     "VALUES(%s,%s,%s,%s,%s);"
# ,(title,source,create_date,description,look))

# param ={
#     "title":input("請輸入標題"),
#     "source":input("請輸入新聞"),
#     "create_date":input("請輸入日期"),
#     "description":input("請輸入描述"),
#     "look":input("請輸入瀏覽率")
# }
#
# c.execute(
#     "INSERT INTO news(title,source,create_date,description,look) " +
#     "VALUES(%(title)s,%(source)s,%(create_date)s,%(description)s,%(look)s);"
#  ,param)

param ={
    "id":input("你要del的id"),
}

c.execute(
    "DELETE FROM news WHERE id =%(id)s;"
,param)

link.commit()

link.close()