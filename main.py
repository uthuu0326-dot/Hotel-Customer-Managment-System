import tkinter as tk
from tkinter import messagebox
from database import connect_db


# ---------------- FUNCTIONS ----------------

def add_customer():

    db = connect_db()
    cursor = db.cursor()

    sql = """
    INSERT INTO customers
    (name, phone, room_no)
    VALUES (%s,%s,%s)
    """

    values = (
        name.get(),
        phone.get(),
        room.get()
    )

    cursor.execute(sql, values)

    db.commit()

    cursor.close()
    db.close()

    messagebox.showinfo(
        "Success",
        "Customer Added Successfully ✅"
    )

    clear()



def view_customer():

    db = connect_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM customers"
    )

    rows = cursor.fetchall()

    listbox.delete(0,tk.END)

    for row in rows:
        listbox.insert(
            tk.END,
            row
        )

    cursor.close()
    db.close()



def delete_customer():

    selected = listbox.curselection()

    if selected:

        row = listbox.get(selected[0])

        customer_id = row[0]

        db = connect_db()
        cursor = db.cursor()

        cursor.execute(
            "DELETE FROM customers WHERE id=%s",
            (customer_id,)
        )

        db.commit()

        cursor.close()
        db.close()

        messagebox.showinfo(
            "Deleted",
            "Customer Deleted 🗑"
        )

        view_customer()



def update_customer():

    selected = listbox.curselection()

    if selected:

        row = listbox.get(selected[0])

        customer_id = row[0]

        db = connect_db()
        cursor = db.cursor()

        sql = """
        UPDATE customers
        SET name=%s,
        phone=%s,
        room_no=%s
        WHERE id=%s
        """

        values = (
            name.get(),
            phone.get(),
            room.get(),
            customer_id
        )

        cursor.execute(sql,values)

        db.commit()

        cursor.close()
        db.close()

        messagebox.showinfo(
            "Update",
            "Customer Updated ✏️"
        )

        view_customer()



def clear():

    name.delete(0,tk.END)
    phone.delete(0,tk.END)
    room.delete(0,tk.END)



# ---------------- WINDOW ----------------

window = tk.Tk()

window.title(
    "🏨 Hotel Customer Management System"
)

window.geometry(
    "750x650"
)

window.config(
    bg="#EAF2F8"
)


# ---------------- HEADER ----------------

header = tk.Frame(
    window,
    bg="#1F4E79",
    height=100
)

header.pack(
    fill="x"
)


logo = tk.Label(
    header,
    text="🏨",
    font=("Arial",45),
    bg="#1F4E79",
    fg="white"
)

logo.pack(
    side="left",
    padx=30
)


title = tk.Label(
    header,
    text="Hotel Customer Management System",
    font=("Arial",22,"bold"),
    bg="#1F4E79",
    fg="white"
)

title.pack(
    side="left"
)



# ---------------- FORM FRAME ----------------

form = tk.Frame(
    window,
    bg="white",
    bd=2,
    relief="groove"
)

form.pack(
    pady=20,
    padx=30
)



font_style=("Arial",12,"bold")


tk.Label(
    form,
    text="Customer Name",
    font=font_style,
    bg="white"
).grid(row=0,column=0,padx=10,pady=10)


name=tk.Entry(
    form,
    width=30,
    font=("Arial",12)
)

name.grid(
    row=0,
    column=1
)



tk.Label(
    form,
    text="Phone Number",
    font=font_style,
    bg="white"
).grid(row=1,column=0,padx=10,pady=10)


phone=tk.Entry(
    form,
    width=30,
    font=("Arial",12)
)

phone.grid(
    row=1,
    column=1
)



tk.Label(
    form,
    text="Room Number",
    font=font_style,
    bg="white"
).grid(row=2,column=0,padx=10,pady=10)


room=tk.Entry(
    form,
    width=30,
    font=("Arial",12)
)

room.grid(
    row=2,
    column=1
)



# ---------------- BUTTON FRAME ----------------

button_frame=tk.Frame(
    window,
    bg="#EAF2F8"
)

button_frame.pack()


def create_button(text,command,color):

    return tk.Button(
        button_frame,
        text=text,
        command=command,
        width=18,
        height=2,
        bg=color,
        fg="white",
        font=("Arial",11,"bold")
    )


create_button(
    "➕ Add Customer",
    add_customer,
    "#2E86C1"
).grid(row=0,column=0,padx=5,pady=5)


create_button(
    "👀 View",
    view_customer,
    "#117864"
).grid(row=0,column=1,padx=5,pady=5)


create_button(
    "✏ Update",
    update_customer,
    "#CA6F1E"
).grid(row=1,column=0,padx=5,pady=5)


create_button(
    "🗑 Delete",
    delete_customer,
    "#922B21"
).grid(row=1,column=1,padx=5,pady=5)



# ---------------- LIST ----------------

list_frame=tk.Frame(
    window,
    bg="white"
)

list_frame.pack(
    pady=20
)


listbox=tk.Listbox(
    list_frame,
    width=70,
    height=10,
    font=("Consolas",11)
)

listbox.pack()



window.mainloop()