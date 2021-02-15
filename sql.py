import sqlite3

connection = sqlite3.connect('practice.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS main(
                email TEXT,
                password TEXT,
                SURNAME TEXT,
                NAME_of_user TEXT
)""")

cursor.execute("""INSERT INTO main VALUES('ab@mail.ru','Yorkin','ABDUQAHHOROV','YORQIN')""")

a = str(input("mailni kiriting:"))
b = str(input('PARoLLI kiriting:'))
cursor.execute(
    """SELECT SURNAME,NAME_of_user,email,password FROM main WHERE email='{un}' AND password='{pw}'""".format(un=a,
                                                                                                             pw=b))
result = cursor.fetchall()
print(result[0][1])
if len(result) == 1:
    for i in result:
        print(i[0],i[1]+" WO GAP YO`Q siz muvaffaqiyatlik page ga kirdiz")
    #print("WO GAP YO`Q siz muvaffaqiyatlik page ga kirdiz")
else:
    print("E bo`madi karochi")
