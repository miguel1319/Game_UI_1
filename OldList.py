import pandas as pd
from Connect import *
import xlrd


df = pd.read_excel('C:/Users/mmc13/Desktop/SQL/GameInventory.xls')

def insert_Item(conn,var1,var2,var3):
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO Video_Games(Title,Price) VALUES(?,?);',
        (var1, var2)
    )
    conn.commit()

    cursor.execute(
        'select top(1) Game_ID from Video_Games order by Game_ID desc;'
    )

    last_id = 0
    for i in cursor:
        last_id = int(i[0])

    cursor.execute(
        'INSERT INTO Game_Info(Game_ID,Console_ID) VALUES(?,?);',
        (last_id, var3)
    )
    conn.commit()

count = 0
for i in range(1, 635):
    if isinstance(df.loc[i][1], str) and (df.loc[i][3] == 'Physical ' or df.loc[i][3] == 'Physical'):
        count+=1
        print(df.loc[i][1] + "--" + df.loc[i][2] + "--" + df.loc[i][3] + "--" + str(df.loc[i][4]))
print(count)