from tkinter import *
from tkinter import messagebox, font
import pymysql

# Create the main window
window = Tk()
window.title("Update Password")
window.geometry("400x250")
window.configure(bg="#F0F0F0")

# Set custom font
custom_font = font.Font(family="Helvetica", size=12)

# Function to update password
def update_password():
    email = email_entry.get()
    old_password = old_password_entry.get()
    new_password = new_password_entry.get()

    # Check if all fields are filled
    if email.strip() == "" or old_password.strip() == "" or new_password.strip() == "":
        messagebox.showwarning("Warning", "Please fill in all the fields")
        return

    # Database connection
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Qwerty6118$',
        db='gpt_inv'
    )

    cursor = conn.cursor()

    # Check if old password is correct
    cursor.execute("SELECT * FROM Employee WHERE Email = %s AND PasswordHash = %s", (email, old_password))
    result = cursor.fetchone()

    if result:
        # Update password
        cursor.execute("UPDATE Employee SET PasswordHash = %s WHERE Email = %s", (new_password, email))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Password updated successfully!")
        window.destroy()
    else:
        messagebox.showerror("Error", "Invalid email or old password")

# Function to go back to the login window
def go_back():
    window.destroy()  # Close the current window
    # Open the login window (assuming your login window code is in a file named "login_window.py")
    import login_window
    login_window.main()

# Labels and entry fields for email, old password, and new password
email_label = Label(window, text="Email:", bg="#F0F0F0")
email_label['font'] = custom_font
email_label.grid(row=0, column=0, padx=10, pady=10)
email_entry = Entry(window, bg="white")
email_entry['font'] = custom_font
email_entry.grid(row=0, column=1, padx=10, pady=10)

old_password_label = Label(window, text="Old Password:", bg="#F0F0F0")
old_password_label['font'] = custom_font
old_password_label.grid(row=1, column=0, padx=10, pady=10)
old_password_entry = Entry(window, show="*", bg="white")
old_password_entry['font'] = custom_font
old_password_entry.grid(row=1, column=1, padx=10, pady=10)

new_password_label = Label(window, text="New Password:", bg="#F0F0F0")
new_password_label['font'] = custom_font
new_password_label.grid(row=2, column=0, padx=10, pady=10)
new_password_entry = Entry(window, show="*", bg="white")
new_password_entry['font'] = custom_font
new_password_entry.grid(row=2, column=1, padx=10, pady=10)

# Button to update password
update_button = Button(window, text="Update Password", command=update_password, bg="#007bff", fg="white")
update_button['font'] = custom_font
update_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Back button to go back to login window
back_button = Button(window, text="Back", command=go_back, bg="#007bff", fg="white")
back_button['font'] = custom_font
back_button.grid(row=4, columnspan=2, padx=10, pady=10)

window.mainloop()
