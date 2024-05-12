from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import random
import pymysql
import csv
from datetime import datetime
import threading  # Import threading module

window = tkinter.Tk()
window.title("Inventory Management System")
window.geometry("720x640")
my_tree = ttk.Treeview(window, show='headings', height=20)
style = ttk.Style()

placeholderArray = ['', '', '', '', '', '']
numeric = '1234567890'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Qwerty6118$',
        db='gpt_inv'
    )
    return conn


conn = connection()
cursor = conn.cursor()


for i in range(0, 6):
    placeholderArray[i] = tkinter.StringVar()


def read():
    cursor.connection.ping()
    sql = f"SELECT `ProductID`, `Name`, `Price`, `Quantity`, `Category`, `Description` FROM Product ORDER BY `ProductID` DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")
    my_tree.tag_configure('orow', background="#EEEEEE")
    my_tree.pack()


def setph(word, num):
    for ph in range(0, 6):
        if ph == num:
            placeholderArray[ph].set(word)


def save():
    ProductID = str(ProductIDEntry.get())
    Name = str(NameEntry.get())
    Price = str(PriceEntry.get())
    Quantity = str(QuantityEntry.get())
    Category = str(CategoryCombo.get())
    Description = str(DescriptionEntry.get("1.0", END))
    if not ProductID.isdigit() or len(ProductID) != 2:
        messagebox.showwarning("", "Invalid Product ID. Please enter a 5-digit numeric ID.")
        return
    if not (ProductID and ProductID.strip()) or not (Name and Name.strip()) or not (Price and Price.strip()) or not (
            Quantity and Quantity.strip()) or not (Category and Category.strip()) or not (
            Description and Description.strip()):
        messagebox.showwarning("", "Please fill up all entries")
        return
    try:
        cursor.connection.ping()
        sql = f"SELECT * FROM Product WHERE `ProductID` = '{ProductID}' "
        cursor.execute(sql)
        checkProductNo = cursor.fetchall()
        if len(checkProductNo) > 0:
            messagebox.showwarning("", "Product ID already used")
            return
        else:
            cursor.connection.ping()
            sql = f"INSERT INTO Product (`ProductID`, `Name`, `Price`, `Quantity`, `Category`, `Description`) VALUES ('{ProductID}','{Name}','{Price}','{Quantity}','{Category}','{Description}')"
            cursor.execute(sql)
        conn.commit()
        conn.close()
        for num in range(0, 6):
            setph('', (num))
    except Exception as e:
        print(e)
        messagebox.showwarning("", "Error while saving ref: " + str(e))
        return
    refreshTable()


def update():
    selectedProductID = ''
    try:
        selectedItem = my_tree.selection()[0]
        selectedProductID = str(my_tree.item(selectedItem)['values'][0])
    except:
        messagebox.showwarning("", "Please select a data row")
    print(selectedProductID)
    ProductID = str(ProductIDEntry.get())
    Name = str(NameEntry.get())
    Price = str(PriceEntry.get())
    Quantity = str(QuantityEntry.get())
    Category = str(CategoryCombo.get())
    Description = str(DescriptionEntry.get("1.0", END))
    if not (ProductID and ProductID.strip()) or not (Name and Name.strip()) or not (Price and Price.strip()) or not (
            Quantity and Quantity.strip()) or not (Category and Category.strip()) or not (
            Description and Description.strip()):
        messagebox.showwarning("", "Please fill up all entries")
        return
    if selectedProductID != ProductID:
        messagebox.showwarning("", "You can't change Product ID")
        return
    try:
        cursor.connection.ping()
        sql = f"UPDATE Product SET `Name` = '{Name}', `Price` = '{Price}', `Quantity` = '{Quantity}', `Category` = '{Category}', `Description` = '{Description}' WHERE `ProductID` = '{ProductID}' "
        cursor.execute(sql)
        conn.commit()
        conn.close()
        for num in range(0, 6):
            setph('', (num))
    except Exception as err:
        messagebox.showwarning("", "Error occured ref: " + str(err))
        return
    refreshTable()


def delete():
    try:
        if (my_tree.selection()[0]):
            decision = messagebox.askquestion("", "Delete the selected data?")
            if (decision != 'yes'):
                return
            else:
                selectedItem = my_tree.selection()[0]
                ProductID = str(my_tree.item(selectedItem)['values'][0])
                try:
                    cursor.connection.ping()
                    sql = f"DELETE FROM Product WHERE `ProductID` = '{ProductID}' "
                    cursor.execute(sql)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("", "Data has been successfully deleted")
                except:
                    messagebox.showinfo("", "Sorry, an error occured")
                refreshTable()
    except:
        messagebox.showwarning("", "Please select a data row")


def select():
    try:
        selectedItem = my_tree.selection()[0]
        ProductID = str(my_tree.item(selectedItem)['values'][0])
        Name = str(my_tree.item(selectedItem)['values'][1])
        Price = str(my_tree.item(selectedItem)['values'][2])
        Quantity = str(my_tree.item(selectedItem)['values'][3])
        Category = str(my_tree.item(selectedItem)['values'][4])
        Description = str(my_tree.item(selectedItem)['values'][5])
        setph(ProductID, 0)
        setph(Name, 1)
        setph(Price, 2)
        setph(Quantity, 3)
        setph(Category, 4)
        DescriptionEntry.delete("1.0", END)
        DescriptionEntry.insert("1.0", Description)
    except:
        messagebox.showwarning("", "Please select a data row")


def find():
    ProductID = str(ProductIDEntry.get())
    Name = str(NameEntry.get())
    Price = str(PriceEntry.get())
    Quantity = str(QuantityEntry.get())
    Category = str(CategoryCombo.get())
    cursor.connection.ping()
    if (ProductID and ProductID.strip()):
        sql = f"SELECT `ProductID`, `Name`, `Price`, `Quantity`, `Category`, `Description` FROM Product WHERE `ProductID` LIKE '%{ProductID}%' "
    elif (Name and Name.strip()):
        sql = f"SELECT `ProductID`, `Name`, `Price`, `Quantity`, `Category`, `Description` FROM Product WHERE `Name` LIKE '%{Name}%' "
    elif (Price and Price.strip()):
        sql = f"SELECT `ProductID`, `Name`, `Price`, `Quantity`, `Category`, `Description` FROM Product WHERE `Price` LIKE '%{Price}%' "
    elif (Quantity and Quantity.strip()):
        sql = f"SELECT `ProductID`, `Name`, `Price`, `Quantity`, `Category`, `Description` FROM Product WHERE `Quantity` LIKE '%{Quantity}%' "
    elif (Category and Category.strip()):
        sql = f"SELECT `ProductID`, `Name`, `Price`, `Quantity`, `Category`, `Description` FROM Product WHERE `Category` LIKE '%{Category}%' "
    else:
        messagebox.showwarning("", "Please fill up one of the entries")
        return
    cursor.execute(sql)
    try:
        result = cursor.fetchall();
        for num in range(0, 6):
            setph(result[0][num], (num))
        DescriptionEntry.delete("1.0", END)
        DescriptionEntry.insert("1.0", result[0][5])
        conn.commit()
        conn.close()
    except:
        messagebox.showwarning("", "No data found")


def clear():
    for num in range(0, 6):
        setph('', (num))
    DescriptionEntry.delete("1.0", END)


def exportExcel():
    cursor.connection.ping()
    sql = f"SELECT `ProductID`, `Name`, `Price`, `Quantity`, `Category`, `Description` FROM Product ORDER BY `ProductID` DESC"
    cursor.execute(sql)
    dataraw = cursor.fetchall()
    date = str(datetime.now())
    date = date.replace(' ', '_')
    date = date.replace(':', '-')
    dateFinal = date[0:16]
    with open("products_" + dateFinal + ".csv", 'a', newline='') as f:
        w = csv.writer(f, dialect='excel')
        for record in dataraw:
            w.writerow(record)
    print("saved: products_" + dateFinal + ".csv")
    conn.commit()
    conn.close()
    messagebox.showinfo("", "Excel file downloaded")


def refresh_data():
    while True:
        refreshTable()
        # Refresh every 10 seconds
        threading.Timer(10, refresh_data).start()


def start_refresh_thread():
    # Start the thread for periodic refresh
    threading.Thread(target=refresh_data).start()


frame = tkinter.Frame(window, bg="#02577A")
frame.pack()

btnColor = "#196E78"

manageFrame = tkinter.LabelFrame(frame, text="Manage", borderwidth=5)
manageFrame.grid(row=0, column=0, sticky="w", padx=[10, 200], pady=20, ipadx=[6])

saveBtn = Button(manageFrame, text="SAVE", width=10, borderwidth=3, bg=btnColor, fg='white', command=save)
updateBtn = Button(manageFrame, text="UPDATE", width=10, borderwidth=3, bg=btnColor, fg='white', command=update)
deleteBtn = Button(manageFrame, text="DELETE", width=10, borderwidth=3, bg=btnColor, fg='white', command=delete)
selectBtn = Button(manageFrame, text="SELECT", width=10, borderwidth=3, bg=btnColor, fg='white', command=select)
findBtn = Button(manageFrame, text="FIND", width=10, borderwidth=3, bg=btnColor, fg='white', command=find)
clearBtn = Button(manageFrame, text="CLEAR", width=10, borderwidth=3, bg=btnColor, fg='white', command=clear)
exportBtn = Button(manageFrame, text="EXPORT EXCEL", width=15, borderwidth=3, bg=btnColor, fg='white',
                   command=exportExcel)

saveBtn.grid(row=0, column=0, padx=5, pady=5)
updateBtn.grid(row=0, column=1, padx=5, pady=5)
deleteBtn.grid(row=0, column=2, padx=5, pady=5)
selectBtn.grid(row=0, column=3, padx=5, pady=5)
findBtn.grid(row=0, column=4, padx=5, pady=5)
clearBtn.grid(row=0, column=5, padx=5, pady=5)
exportBtn.grid(row=0, column=6, padx=5, pady=5)

entriesFrame = tkinter.LabelFrame(frame, text="Form", borderwidth=5)
entriesFrame.grid(row=1, column=0, sticky="w", padx=[10, 200], pady=[0, 20], ipadx=[6])

ProductIDLabel = Label(entriesFrame, text="PRODUCT ID", anchor="e", width=10)
NameLabel = Label(entriesFrame, text="NAME", anchor="e", width=10)
PriceLabel = Label(entriesFrame, text="PRICE", anchor="e", width=10)
QuantityLabel = Label(entriesFrame, text="QUANTITY", anchor="e", width=10)
CategoryLabel = Label(entriesFrame, text="CATEGORY", anchor="e", width=10)
DescriptionLabel = Label(entriesFrame, text="DESCRIPTION", anchor="e", width=10)

ProductIDLabel.grid(row=0, column=0, padx=10)
NameLabel.grid(row=1, column=0, padx=10)
PriceLabel.grid(row=2, column=0, padx=10)
QuantityLabel.grid(row=3, column=0, padx=10)
CategoryLabel.grid(row=4, column=0, padx=10)
DescriptionLabel.grid(row=5, column=0, padx=10)

categoryArray = ['Networking Tools', 'Computer Parts', 'Repair Tools', 'Gadgets']

ProductIDEntry = Entry(entriesFrame, width=50, textvariable=placeholderArray[0])
NameEntry = Entry(entriesFrame, width=50, textvariable=placeholderArray[1])
PriceEntry = Entry(entriesFrame, width=50, textvariable=placeholderArray[2])
QuantityEntry = Entry(entriesFrame, width=50, textvariable=placeholderArray[3])
CategoryCombo = ttk.Combobox(entriesFrame, width=47, textvariable=placeholderArray[4], values=categoryArray)
DescriptionEntry = Text(entriesFrame, width=47, height=5)

ProductIDEntry.grid(row=0, column=1, padx=5, pady=5)
NameEntry.grid(row=1, column=1, padx=5, pady=5)
PriceEntry.grid(row=2, column=1, padx=5, pady=5)
QuantityEntry.grid(row=3, column=1, padx=5, pady=5)
CategoryCombo.grid(row=4, column=1, padx=5, pady=5)
DescriptionEntry.grid(row=5, column=1, padx=5, pady=5)

style.configure(window)
my_tree['columns'] = ("ProductID", "Name", "Price", "Quantity", "Category", "Description")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ProductID", anchor=W, width=70)
my_tree.column("Name", anchor=W, width=125)
my_tree.column("Price", anchor=W, width=125)
my_tree.column("Quantity", anchor=W, width=100)  # Set width for Quantity column
my_tree.column("Category", anchor=W, width=150)
my_tree.column("Description", anchor=W, width=150)
my_tree.heading("ProductID", text="ProductID", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Price", text="Price", anchor=W)
my_tree.heading("Quantity", text="Quantity", anchor=W)  # Set heading for Quantity column
my_tree.heading("Category", text="Category", anchor=W)
my_tree.heading("Description", text="Description", anchor=W)
my_tree.tag_configure('orow', background="#EEEEEE")
my_tree.pack()

refreshTable()

window.resizable(False, False)



window.mainloop()
