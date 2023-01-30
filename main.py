from Connect import *
from Functions import *
from tkinter import *

# Start UI Design

# Set Up
root = Tk()
root.state("zoomed")
root.title("Video Game Inventory Editor")
root.iconbitmap('GameIcon.ico')

# Creating and Displaying Widgets
myLabel = Label(root, text="Welcome  to  the  Video_Game_Editor", font="BOLD")
myLabel.grid(row=0, column=1, pady=20)

Text_Widget = Text(root, height=20, width=100)

Text_Widget.grid(row=1, column=1, padx=10, pady=10)


# insert frame
frame_insert = LabelFrame(root, text="Insert Game", padx=100, pady=10)
frame_insert.grid(row=2, column=1)

entry_Title = Entry(frame_insert)
entry_Title.pack()

titleLabel = Label(frame_insert, text="Title")
titleLabel.pack()

entry_Price = Entry(frame_insert)
entry_Price.pack()

priceLabel = Label(frame_insert, text="Price")
priceLabel.pack()

insert_Button = Button(frame_insert, text="Insert into Table", padx=30, pady=5, command=lambda: insert_Item(conn, entry_Title, entry_Price))
insert_Button.pack()

# delete frame
delete_frame = LabelFrame(root, text="Delete Game", padx=100, pady=10)
delete_frame.grid(row=3, column=1, pady=10)

delete_entry = Entry(delete_frame)
delete_entry.pack()

delete_label = Label(delete_frame, text="ID of game", pady=5)
delete_label.pack()

del_button = Button(delete_frame, text="Delete", padx=30, pady=1, command=lambda: delete_item(delete_entry, conn))
del_button.pack()

# update frame
update_frame = LabelFrame(root, text="Update Game", padx=10, pady=10)
update_frame.grid(row=2, rowspan=3, column=0, padx=100)

up_entry = Entry(update_frame)
up_entry.pack()

up_label = Label(update_frame, text="ID of Game", pady=5)
up_label.pack()

up_entry_var = Entry(update_frame)
up_entry_var.pack()


update_clicked = StringVar()
update_clicked.set("Select a field")
update_drop_menu = OptionMenu(update_frame, update_clicked, "Title", "Price")
update_drop_menu.pack(pady=5)


up_button = Button(update_frame, text="Update", command=lambda : update_item(conn, update_clicked, up_entry, up_entry_var))
up_button.pack()

# find frame
find_frame = LabelFrame(root, text="Find Game", padx=10, pady=10)
find_frame.grid(row=2, rowspan=3, column=2, padx=100)


find_entry_var = Entry(find_frame)
find_entry_var.pack()

clicked = StringVar()
clicked.set("Select a field")
find_drop_menu = OptionMenu(find_frame, clicked, "Game ID", "Title", "Price")
find_drop_menu.pack(pady=5)

find_button = Button(find_frame, text="Find", command=lambda: find_item(conn, clicked,find_entry_var,Text_Widget))
find_button.pack()
# frames end

Read_Button = Button(root, text="Read Function", padx=30, pady=5, command=lambda: read_to_screen(conn, Text_Widget)).grid(row=4, column=1)
Clear_Button = Button(root, text="Clear Text", padx=30, pady=5, command=lambda: clear(Text_Widget)).grid(row=5, column=1, pady=5)

# main loop
root.mainloop()
