import tkinter


def read_to_console(conn):
    print("read")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Video_Games")
    for row in cursor:
        print(f'row = {row}')
    print()


def insert_into_table(conn):
    print("insert")
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO Video_Games(Title,Price) VALUES(?,?);',
        ('Cuphead',40)
    )
    conn.commit()


def update(conn):
    print("update")
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE Video_Games SET Price = ? WHERE Title = ?;',
        (100, 'Cuphead')
    )
    conn.commit()


def delete(conn):

    print("delete")
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM Video_Games WHERE Title = ?;',
        ('Cuphead')
    )
    conn.commit()


def read_to_screen(conn, text_widget):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Video_Games")
    count=0
    for row in cursor:
        count = count+1
        text_widget.insert(tkinter.END, str(count) + " - ")
        x = 0
        for i in row:
            x = x + 1
            g = str(i)
            if x == 3:
                text_widget.insert(tkinter.END, "$" + g)
                break
            text_widget.insert(tkinter.END, g)
            text_widget.insert(tkinter.END, " - ")
        text_widget.insert(tkinter.END, "\n")


def ListBox_Display(conn, text_widget):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Video_Games")
    count = 0
    display_string = ""
    for row in cursor:
        count = count + 1
        display_string = display_string + str(count) + " - "
        x = 0
        for i in row:
            x = x + 1
            g = str(i)
            if x == 3:
                display_string = display_string + "$" + g
                break
            display_string = display_string + g
            display_string = display_string + " - "
        text_widget.insert(tkinter.END, display_string)
        display_string = ""


def clear(text):
    text.delete("1.0", "end")


def take_Name(Text):
    var = Text.get()
    print(var)


def insert_Item(conn, title, price):
    var1 = title.get()
    var2 = int(price.get())
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO Video_Games(Title,Price) VALUES(?,?);',
        (var1, var2)
    )
    conn.commit()


def delete_item(number, conn):

    var = int(number.get())
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM Video_Games WHERE Game_ID = ?;',
        (var)
    )
    conn.commit()


def find_item(conn, clicked, find_var, text_widget):
    var = clicked.get()
    if var == "Select a field":
        return
    elif var == "Title":
        print("you selected title")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Video_Games")
        count = 0
        for row in cursor:
            if find_var.get().lower() in row[1].lower():
                count = count + 1
                text_widget.insert(tkinter.END, str(count) + " - ")
                x = 0
                for i in row:
                    x = x + 1
                    g = str(i)
                    if x == 3:
                        text_widget.insert(tkinter.END, "$" + g)
                        break
                    text_widget.insert(tkinter.END, g)
                    text_widget.insert(tkinter.END, " - ")
                text_widget.insert(tkinter.END, "\n")

    elif var == "Price":
        print("You selected price")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Video_Games")
        count = 0
        for row in cursor:
            if int(find_var.get()) == row[2]:
                count = count + 1
                text_widget.insert(tkinter.END, str(count) + " - ")
                x = 0
                for i in row:
                    x = x + 1
                    g = str(i)
                    if x == 3:
                        text_widget.insert(tkinter.END, "$" + g)
                        break
                    text_widget.insert(tkinter.END, g)
                    text_widget.insert(tkinter.END, " - ")
                text_widget.insert(tkinter.END, "\n")

    elif var == "Game ID":
        print("You selected Game ID")


def update_item(conn, clicked, ID, up_entry_var):
    var = clicked.get()
    var_id = int(ID.get())
    var_updated = up_entry_var.get()
    if var == "Select a field":
        return
    elif var == "Title":
        print("you selected title")
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE Video_Games SET Title = ? WHERE Game_ID = ?;',
            (var_updated, var_id)
        )
        conn.commit()

    elif var == "Price":
        print("You selected price")

        cursor = conn.cursor()
        cursor.execute(
            'UPDATE Video_Games SET Price = ? WHERE Game_ID = ?;',
            (int(var_updated), var_id)
        )
        conn.commit()



