from tkinter import *
from tkinter import messagebox, font
import pymysql

# Create the main window
window = Tk()
window.title("Login")
window.geometry("400x200")
window.configure(bg="#F0F0F0")

# Set custom font
custom_font = font.Font(family="Helvetica", size=12)

# Database connection
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Qwerty6118$',
        db='gpt_inv'
    )
    return conn

# Function to check login credentials
def login():
    email = email_entry.get()
    password = password_entry.get()

    # Check if email and password are provided
    if email.strip() == "" or password.strip() == "":
        messagebox.showwarning("Warning", "Please enter both email and password")
        return

    # Check if employee exists and password is correct
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employee WHERE Email = %s AND PasswordHash = %s", (email, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Success", "Login successful!")
        window.destroy()  # Close login window
        # Add your code here to open the main menu window or another window
    else:
        messagebox.showerror("Error", "Invalid email or password")

# Entry fields for email and password
email_label = Label(window, text="Email:", bg="#F0F0F0")
email_label['font'] = custom_font
email_label.grid(row=0, column=0, padx=10, pady=10)
email_entry = Entry(window, bg="white")
email_entry['font'] = custom_font
email_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = Label(window, text="Password:", bg="#F0F0F0")
password_label['font'] = custom_font
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = Entry(window, show="*", bg="white")
password_entry['font'] = custom_font
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Button to login
login_button = Button(window, text="Login", command=login, bg="#007bff", fg="white")
login_button['font'] = custom_font
login_button.grid(row=2, columnspan=2, padx=10, pady=10)

window.mainloop()
