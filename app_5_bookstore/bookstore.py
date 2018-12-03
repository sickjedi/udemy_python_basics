from tkinter import *
from backend import Database


database = Database()

def clear_entry_fileds():
    title_entry.delete(0, END)
    author_entry.delete(0, END)
    year_entry.delete(0, END)
    isbn_entry.delete(0, END)


def fill_entry_fileds(selected_book):
    clear_entry_fileds()
    title_entry.insert(END, selected_book[1])
    author_entry.insert(END, selected_book[2])
    year_entry.insert(END, selected_book[3])
    isbn_entry.insert(END, selected_book[4])


def get_selected_row(evt):
    try:
        global selected_book
        index = book_list.curselection()[0]
        selected_book = book_list.get(index)
        fill_entry_fileds(selected_book)
    except IndexError:
        pass


def view_all_command():
    book_list.delete(0, END)
    for book in database.view():
        book_list.insert(END, book)


def search_command():
    book_list.delete(0, END)
    for book in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        book_list.insert(END, book)


def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_all_command()


def update_command():
    database.update(selected_book[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_all_command()


def delete_command():
    database.delete(selected_book[0])
    view_all_command()

window = Tk()

title_label = Label(window, text="Title")
title_label.grid(row=0, column=0)

author_label = Label(window, text="Author")
author_label.grid(row=0, column=2)

year_label = Label(window, text="Year")
year_label.grid(row=1, column=0)

isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=1, column=2)

title_text = StringVar()
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row=0, column=1)

author_text = StringVar()
author_entry = Entry(window, textvariable=author_text)
author_entry.grid(row=0, column=3)

year_text = StringVar()
year_entry = Entry(window, textvariable=year_text)
year_entry.grid(row=1, column=1)

isbn_text = StringVar()
isbn_entry = Entry(window, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)

book_list = Listbox(window, height=6, width=35)
book_list.grid(row=2, column=0, rowspan=6, columnspan=2)

book_list_scrollbar = Scrollbar(window)
book_list_scrollbar.grid(row=2, column=2, rowspan=6)

book_list.configure(yscrollcommand=book_list_scrollbar.set)
book_list_scrollbar.configure(command=book_list.yview)

book_list.bind('<<ListboxSelect>>', get_selected_row)

view_all_button = Button(window, text="View all", width=12, command=view_all_command)
view_all_button.grid(row=2, column=3)

search_button = Button(window, text="Search entry", width=12, command=search_command)
search_button.grid(row=3, column=3)

add_button = Button(window, text="Add entry", width=12, command=add_command)
add_button.grid(row=4, column=3)

update_button = Button(window, text="Update", width=12, command=update_command)
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete", width=12, command=delete_command)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=12)
close_button.grid(row=7, column=3)

window.mainloop()
