import tkinter as tk
from tkinter import ttk, messagebox
import pymysql

class CustomerOrderPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Customer Order Page")
        self.geometry("800x600")

        self.customerID = tk.StringVar()
        self.customerName = tk.StringVar()
        self.productID = tk.StringVar()
        self.productName = tk.StringVar()
        self.description = tk.StringVar()
        self.price = tk.StringVar()
        self.quantity = tk.IntVar(value=1)
        self.totalPrice = tk.StringVar()

        self.order_list = []

        self.create_widgets()

    def create_widgets(self):
        customer_frame = ttk.LabelFrame(self, text="Customer Details")
        customer_frame.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Label(customer_frame, text="Customer ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(customer_frame, textvariable=self.customerID).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(customer_frame, text="Customer Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(customer_frame, textvariable=self.customerName).grid(row=1, column=1, padx=5, pady=5)

        product_frame = ttk.LabelFrame(self, text="Product Details")
        product_frame.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Label(product_frame, text="Product ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(product_frame, textvariable=self.productID).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(product_frame, text="Search", command=self.search_product).grid(row=0, column=2, padx=5, pady=5)

        tk.Label(product_frame, text="Product Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(product_frame, textvariable=self.productName, state="readonly").grid(row=1, column=1, padx=5, pady=5)

        tk.Label(product_frame, text="Description:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(product_frame, textvariable=self.description, state="readonly").grid(row=2, column=1, padx=5, pady=5)

        tk.Label(product_frame, text="Price:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(product_frame, textvariable=self.price, state="readonly").grid(row=3, column=1, padx=5, pady=5)

        tk.Label(product_frame, text="Quantity:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.quantity_spinbox = tk.Spinbox(product_frame, from_=1, to=100, textvariable=self.quantity)
        self.quantity_spinbox.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(product_frame, text="Total Price:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(product_frame, textvariable=self.totalPrice, state="readonly").grid(row=5, column=1, padx=5, pady=5)

        tk.Button(product_frame, text="Add to Cart", command=self.add_to_cart).grid(row=6, column=1, padx=5, pady=5)

        order_frame = ttk.LabelFrame(self, text="Order Details")
        order_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.order_table = ttk.Treeview(order_frame, columns=("Product ID", "Product Name", "Description", "Price", "Quantity", "Total Price"), show="headings")
        self.order_table.heading("Product ID", text="Product ID")
        self.order_table.heading("Product Name", text="Product Name")
        self.order_table.heading("Description", text="Description")
        self.order_table.heading("Price", text="Price")
        self.order_table.heading("Quantity", text="Quantity")
        self.order_table.heading("Total Price", text="Total Price")

        self.order_table.column("Product ID", width=100)
        self.order_table.column("Product Name", width=150)
        self.order_table.column("Description", width=200)
        self.order_table.column("Price", width=100)
        self.order_table.column("Quantity", width=100)
        self.order_table.column("Total Price", width=100)

        self.order_table.pack(padx=10, pady=10, fill="both", expand=True)

        place_order_button = tk.Button(self, text="Place Order", command=self.place_order)
        place_order_button.pack(padx=10, pady=10, anchor="ne")

    def search_product(self):
        product_id = self.productID.get()
        if not product_id:
            messagebox.showerror("Error", "Please enter a product ID!")
            return

        conn = self.connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT Name, Description, Price, Quantity FROM Product WHERE ProductID = '{product_id}'")
            result = cursor.fetchone()
            conn.close()

            if result:
                self.productName.set(result[0])
                self.description.set(result[1])
                self.price.set(result[2])
                self.calculate_total_price()
                # Update the maximum value for the quantity Spinbox based on available quantity
                self.quantity_spinbox.config(to=result[3])
            else:
                messagebox.showerror("Error", "Product not found!")

    def calculate_total_price(self):
        try:
            price = float(self.price.get())
            quantity = int(self.quantity.get())
            total_price = price * quantity
            self.totalPrice.set(total_price)
        except ValueError:
            messagebox.showerror("Error", "Invalid price or quantity!")

    def add_to_cart(self):
        product_id = self.productID.get()
        product_name = self.productName.get()
        description = self.description.get()
        price_str = self.price.get()
        quantity = int(self.quantity.get())

        if not product_id:
            messagebox.showerror("Error", "Please enter a product ID!")
            return

        if not product_name:
            messagebox.showerror("Error", "Product name is empty!")
            return

        if not description:
            messagebox.showerror("Error", "Product description is empty!")
            return

        if not price_str:
            messagebox.showerror("Error", "Product price is empty!")
            return

        try:
            price = float(price_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid product price!")
            return

        total_price = price * quantity

        self.order_table.insert("", "end", values=(product_id, product_name, description, price, quantity, total_price))
        self.order_list.append((product_id, quantity))

        self.productID.set("")
        self.productName.set("")
        self.description.set("")
        self.price.set("")
        self.quantity.set(1)
        self.totalPrice.set("")

    def place_order(self):
        print("Placing order...")

        if not self.order_list:
            messagebox.showerror("Error", "No items in the order!")
            return

        if not self.customerID.get() or not self.customerName.get():
            messagebox.showerror("Error", "Please enter customer ID and name!")
            return

        conn = self.connect_to_database()
        if conn:
            print("Database connection established.")

            try:
                cursor = conn.cursor()

                # Retrieve customer ID based on entered customer ID or name
                cursor.execute(f"SELECT CustomerID FROM Customer WHERE CustomerID = '{self.customerID.get()}' OR FullName = '{self.customerName.get()}'")
                customer = cursor.fetchone()

                if not customer:
                    messagebox.showerror("Error", "Customer not found!")
                    conn.close()
                    return

                customer_id = customer[0]

                # Check if the ordered quantity is available in the inventory
                for item in self.order_list:
                    product_id, quantity = item
                    cursor.execute(f"SELECT Quantity FROM Product WHERE ProductID = '{product_id}'")
                    available_quantity = cursor.fetchone()[0]
                    if quantity > available_quantity:
                        messagebox.showerror("Error", f"Ordered quantity exceeds available quantity for Product ID: {product_id}")
                        conn.close()
                        return

                # Calculate total amount
                total_amount = sum(item[1] for item in self.order_list)

                # Insert order into Order table using parameterized query
                cursor.execute("INSERT INTO `Order` (CustomerID, TotalAmount) VALUES (%s, %s)", (customer_id, total_amount))
                order_id = cursor.lastrowid

                print("Order inserted successfully.")

                # Insert order items into Order_Product table
                for item in self.order_list:
                    product_id, quantity = item
                    cursor.execute(f"INSERT INTO Order_Product (OrderID, ProductID, Quantity) VALUES ('{order_id}', '{product_id}', '{quantity}')")

                    # Update product quantity in the Product table
                    cursor.execute(f"UPDATE Product SET Quantity = Quantity - {quantity} WHERE ProductID = '{product_id}'")
                    print(f"Product quantity updated for ProductID: {product_id}")

                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Order placed successfully!")
                self.order_list.clear()
            except pymysql.Error as e:
                messagebox.showerror("Database Error", f"Error placing order: {e}")

    def connect_to_database(self):
        try:
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='Qwerty6118$',
                db='gpt_inv'
            )
            return conn
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
            return None

if __name__ == "__main__":
    app = CustomerOrderPage()
    app.mainloop()
