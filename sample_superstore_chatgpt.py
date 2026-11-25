import tkinter as tk
from tkinter import ttk, messagebox

# Product Prices
list_items_1 = {
    "rice": 120, "sugar": 20, "oil": 250, 
    "salt": 25, "paneer": 200, "maggie": 12, "boost": 280
}

items_bought = []

def add_item():
    product = product_var.get().strip().lower()
    try:
        quantity = int(quantity_entry.get())
        if quantity <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive quantity number.")
        return

    if product not in list_items_1:
        messagebox.showerror("Error", f"{product} is not available!")
        return

    price = list_items_1[product]
    total = price * quantity
    items_bought.append((product.capitalize(), quantity, price, total))

    # Add to Table Display
    tree.insert("", "end", values=(len(items_bought), product.capitalize(), quantity, f"Rs {price}", f"Rs {total}"))
    quantity_entry.delete(0, tk.END)

def generate_bill():
    customer_name = name_entry.get().strip()
    if not customer_name:
        messagebox.showerror("Error", "Please enter Customer Name")
        return
    if not items_bought:
        messagebox.showerror("Error", "No items added to bill!")
        return

    subtotal = sum(item[3] for item in items_bought)
    tax = (subtotal * 12) / 100
    final = subtotal + tax

    discount_percent = 0
    if 2000 <= final <= 2999:
        discount_percent = 5
    elif 3000 <= final <= 4999:
        discount_percent = 10
    elif final >= 5000:
        discount_percent = 20

    discount_amt = (final * discount_percent) / 100
    grand_total = final - discount_amt

    receipt = f"""==================================================
                 Vamsi Krishna Store
                     Cherukupalli
==================================================
Customer Name: {customer_name}
--------------------------------------------------
Subtotal:          Rs {subtotal:.2f}
Tax (12%):         Rs {tax:.2f}
Discount ({discount_percent}%):      Rs {discount_amt:.2f}
--------------------------------------------------
GRAND TOTAL:       Rs {grand_total:.2f}
==================================================
              Thank you & Visit again!
"""
    receipt_text.delete("1.0", tk.END)
    receipt_text.insert(tk.END, receipt)

# Window Setup
root = tk.Tk()
root.title("Super Market Bill Generator")
root.geometry("650x650")

# Input Section
frame_top = tk.Frame(root, pady=10)
frame_top.pack()

tk.Label(frame_top, text="Customer Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame_top)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_top, text="Select Item:").grid(row=1, column=0, padx=5, pady=5)
product_var = tk.StringVar(value="rice")
product_dropdown = ttk.Combobox(frame_top, textvariable=product_var, values=list(list_items_1.keys()))
product_dropdown.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_top, text="Quantity:").grid(row=2, column=0, padx=5, pady=5)
quantity_entry = tk.Entry(frame_top)
quantity_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Button(frame_top, text="Add Item", command=add_item, bg="#4CAF50", fg="white").grid(row=3, column=0, columnspan=2, pady=10, sticky="we")

# Cart Table
cols = ("S.No", "Item", "Quantity", "Price", "Total")
tree = ttk.Treeview(root, columns=cols, show="headings", height=6)
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")
tree.pack(pady=10)

# Generate Bill Button
tk.Button(root, text="Generate Bill", command=generate_bill, bg="#2196F3", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

# Receipt Output Box
receipt_text = tk.Text(root, height=12, width=60)
receipt_text.pack(pady=10)

root.mainloop()