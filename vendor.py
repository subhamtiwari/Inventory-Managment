import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
import random

class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Vendor")

        # Main Frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)

        # Place Order Button
        self.place_order_button = ttk.Button(self.main_frame, text="Place Order", command=self.place_order)
        self.place_order_button.grid(row=0, column=0, padx=10, pady=10)

        # Vendor Details Button
        self.vendor_details_button = ttk.Button(self.main_frame, text="Vendor Details", command=self.redirect_to_vendor_details)
        self.vendor_details_button.grid(row=0, column=1, padx=10, pady=10)

        # Back Button
        self.back_button = ttk.Button(self.main_frame, text="Back", command=self.redirect_to_main_menu)
        self.back_button.grid(row=1, columnspan=2, padx=10, pady=10)

    def place_order(self):
        # Instantiate PlaceOrderPage and open it
        place_order_window = tk.Toplevel(self.root)
        place_order_page = PlaceOrderPage(place_order_window)

    def redirect_to_vendor_details(self):
        # Instantiate VendorDetailsPage and open it
        vendor_details_window = tk.Toplevel(self.root)
        vendor_details_page = VendorDetailsPage(vendor_details_window)

    def redirect_to_main_menu(self):
        self.root.destroy()  # Destroy the current window, returning to the main menu

class VendorDetailsPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Vendor Details")

        # Main Frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)

        # Fetch vendors from database and display details in a grid view
        self.display_vendor_details()

        # Back Button
        self.back_button = ttk.Button(self.root, text="Back", command=self.go_back)
        self.back_button.pack(side=tk.BOTTOM, pady=10)

    def display_vendor_details(self):
        # Connect to MySQL database
        connection = self.connect_to_database()
        if connection:
            try:
                with connection.cursor() as cursor:
                    # Fetch vendor details
                    cursor.execute("SELECT VendorID, VendorName, ContactPerson, Email FROM Vendor")
                    vendors = cursor.fetchall()

                    if vendors:
                        # Display vendor details in a grid view
                        tk.Label(self.main_frame, text="Vendor ID").grid(row=0, column=0, padx=5, pady=5)
                        tk.Label(self.main_frame, text="Vendor Name").grid(row=0, column=1, padx=5, pady=5)
                        tk.Label(self.main_frame, text="Contact Person").grid(row=0, column=2, padx=5, pady=5)
                        tk.Label(self.main_frame, text="Email").grid(row=0, column=3, padx=5, pady=5)
                        
                        for i, vendor in enumerate(vendors, start=1):
                            tk.Label(self.main_frame, text=vendor[0]).grid(row=i, column=0, padx=5, pady=5)
                            tk.Label(self.main_frame, text=vendor[1]).grid(row=i, column=1, padx=5, pady=5)
                            tk.Label(self.main_frame, text=vendor[2]).grid(row=i, column=2, padx=5, pady=5)
                            tk.Label(self.main_frame, text=vendor[3]).grid(row=i, column=3, padx=5, pady=5)
                    else:
                        messagebox.showerror("Error", "No vendors found in the database.")
            except pymysql.Error as e:
                messagebox.showerror("Database Error", f"Error executing SQL query: {e}")
            finally:
                connection.close()
        else:
            messagebox.showerror("Database Error", "Failed to connect to the database.")

    def connect_to_database(self):
        try:
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='Qwerty6118$',
                db='gpt_inv'
            )
            return connection
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to MySQL database: {e}")
            return None

    def go_back(self):
        self.root.destroy()

class PlaceOrderPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Place Order")

        # Main Frame
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(padx=20, pady=20)

        # Product Name Label and Entry
        tk.Label(self.main_frame, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
        self.product_name_entry = ttk.Combobox(self.main_frame, state="readonly")
        self.product_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Quantity Label and Entry
        tk.Label(self.main_frame, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
        self.quantity_entry = ttk.Entry(self.main_frame)
        self.quantity_entry.grid(row=1, column=1, padx=5, pady=5)

        # Vendor Label and Dropdown
        tk.Label(self.main_frame, text="Vendor:").grid(row=2, column=0, padx=5, pady=5)
        self.vendor_dropdown = ttk.Combobox(self.main_frame, state="readonly")
        self.vendor_dropdown.grid(row=2, column=1, padx=5, pady=5)

        # Place Order Button
        self.place_order_button = ttk.Button(self.main_frame, text="Place Order", command=self.place_order)
        self.place_order_button.grid(row=3, columnspan=2, padx=5, pady=10)

        # Back Button
        self.back_button = ttk.Button(self.main_frame, text="Back", command=self.go_back)
        self.back_button.grid(row=4, columnspan=2, padx=10, pady=10)

        # Populate product and vendor dropdowns
        self.populate_product_dropdown()
        self.populate_vendor_dropdown()

    def place_order(self):
        product_name = self.product_name_entry.get()
        quantity = self.quantity_entry.get()
        vendor_name = self.vendor_dropdown.get()
        if not product_name or not quantity or not vendor_name:
            messagebox.showwarning("Incomplete Information", "Please select a product, enter a quantity, and select a vendor.")
            return

        # Connect to the database
        conn = self.connect_to_database()

        # Get the product ID
        product_id = self.get_product_id(conn, product_name)

        if product_id is None:
            messagebox.showerror("Error", "Selected product not found in the database")
            conn.close()
            return

        # Generate a random order ID
        order_id = self.generate_order_id()

        # Insert the order into the Order_Product table
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Order_Product (OrderID, ProductID, Quantity) VALUES (%s, %s, %s)", (order_id, product_id, quantity))
        conn.commit()

        # Close the database connection
        conn.close()

        # Display success message
        messagebox.showinfo("Success", "Order placed successfully!")

    def populate_product_dropdown(self):
        # Connect to MySQL database
        connection = self.connect_to_database()
        if connection:
            try:
                with connection.cursor() as cursor:
                    # Fetch product names
                    cursor.execute("SELECT Name FROM Product")
                    products = cursor.fetchall()
                    product_names = [product[0] for product in products]
                    self.product_name_entry["values"] = product_names
            except pymysql.Error as e:
                messagebox.showerror("Database Error", f"Error executing SQL query: {e}")
            finally:
                connection.close()
        else:
            messagebox.showerror("Database Error", "Failed to connect to the database.")

    def populate_vendor_dropdown(self):
        # Connect to MySQL database
        connection = self.connect_to_database()
        if connection:
            try:
                with connection.cursor() as cursor:
                    # Fetch vendor names
                    cursor.execute("SELECT VendorName FROM Vendor")
                    vendors = cursor.fetchall()
                    vendor_names = [vendor[0] for vendor in vendors]
                    self.vendor_dropdown["values"] = vendor_names
            except pymysql.Error as e:
                messagebox.showerror("Database Error", f"Error executing SQL query: {e}")
            finally:
                connection.close()
        else:
            messagebox.showerror("Database Error", "Failed to connect to the database.")

    def connect_to_database(self):
        try:
            connection = pymysql.connect(
                host="141.209.241.91",
                user="sp2024bis698g3",
                password="warm",
                database="sp2024bis698g3s",
            )
            return connection
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to MySQL database: {e}")
            return None

    def get_product_id(self, conn, product_name):
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT ProductID FROM Product WHERE Name = %s", (product_name,))
                result = cursor.fetchone()
                if result:
                    return result[0]  # Fetch the first column (ProductID)
                else:
                    return None
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Error executing SQL query: {e}")
            return None

    def generate_order_id(self):
        # Generate a random order ID
        return random.randint(1000, 9999)

    def go_back(self):
        self.master.destroy()  # Destroy the current window, returning to the vendor details page

if __name__ == "__main__":
    root = tk.Tk()
    main_page = MainPage(root)
    root.mainloop()
