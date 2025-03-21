import requests
import json
import tkinter as tk
from tkinter import ttk, messagebox
from utils.helpers import fetch_json_data, send_json_data

# Helper functions
def populate_table(tree, data):
    def clean_value(value):
        return str(value).strip() if isinstance(value, str) else value

    for row in tree.get_children():
        tree.delete(row)

    if isinstance(data, dict):
        tree["columns"] = ("Value",)
        tree.heading("#0", text="Key")
        tree.column("#0", width=150)
        tree.heading("Value", text="Value")
        tree.column("Value", width=250)
        for key, value in data.items():
            tree.insert("", "end", text=key, values=(clean_value(value),))
    elif isinstance(data, list) and data:
        columns = list(data[0].keys())
        tree["columns"] = columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        for item in data:
            tree.insert("", "end", values=[clean_value(item[col]) for col in columns])
    else:
        messagebox.showwarning("Warning", "No tabular data available or invalid JSON.")

def fetch_and_display():
    url = entry_url.get()
    data = fetch_json_data(url)
    if data:
        populate_table(output_tree, data)

def send_data():
    try:
        data = {
            "A": float(entry_a.get()),
            "B": float(entry_b.get()),
            "C": float(entry_c.get()),
            "TYPE": int(entry_type.get()),
            "ORIENTATION": bool(var_orientation.get()),
            "SMALLBOX": bool(var_smallbox.get()),
            "La": int(entry_la.get()),
            "Lb": int(entry_lb.get()),
            "Lc": int(entry_lc.get()),
            "NAME": entry_name.get()[:254]  # Limit string length to 254 characters
        }
        url = entry_url.get()
        response_data = send_json_data(url, data)
        if response_data:
            populate_table(output_tree, response_data)
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# GUI Helper to create labeled entry fields
def create_labeled_entry(parent, label_text, default_value, row, column, width=10):
    tk.Label(parent, text=label_text).grid(row=row, column=column, padx=5, pady=5)
    entry = tk.Entry(parent, width=width)
    entry.insert(0, default_value)
    entry.grid(row=row, column=column + 1, padx=5, pady=5)
    return entry

# Create GUI
root = tk.Tk()
root.title("JSON Data Viewer")
root.geometry("800x600")

# URL Input
tk.Label(root, text="URL:").pack(pady=5)
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)
entry_url.insert(0, "http://192.168.250.1:8080/")

# Input fields for sending data
tk.Label(root, text="Send Data:").pack(pady=5)
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

# Input fields
entry_a = create_labeled_entry(input_frame, "A:", "80.0", 0, 0)
entry_b = create_labeled_entry(input_frame, "B:", "25.0", 1, 0)
entry_c = create_labeled_entry(input_frame, "C:", "15.0", 2, 0)
entry_type = create_labeled_entry(input_frame, "TYPE:", "1", 3, 0)

tk.Label(input_frame, text="ORIENTATION:").grid(row=4, column=0, padx=5, pady=5)
var_orientation = tk.IntVar(value=0)
checkbox_orientation = tk.Checkbutton(input_frame, variable=var_orientation)
checkbox_orientation.grid(row=4, column=1, padx=5, pady=5)

tk.Label(input_frame, text="SMALLBOX:").grid(row=5, column=0, padx=5, pady=5)
var_smallbox = tk.IntVar(value=0)
checkbox_smallbox = tk.Checkbutton(input_frame, variable=var_smallbox)
checkbox_smallbox.grid(row=5, column=1, padx=5, pady=5)

entry_la = create_labeled_entry(input_frame, "La:", "190", 6, 0)
entry_lb = create_labeled_entry(input_frame, "Lb:", "150", 7, 0)
entry_lc = create_labeled_entry(input_frame, "Lc:", "110", 8, 0)
entry_name = create_labeled_entry(input_frame, "NAME:", "ThomasSuperBox", 9, 0, width=30)

# Buttons
tk.Button(root, text="Send Data", command=send_data).pack(pady=10)

# Output table
tk.Label(root, text="Received Data (Table):").pack(pady=5)
output_tree = ttk.Treeview(root)
output_tree.pack(expand=True, fill="both", padx=10, pady=10)
tk.Button(root, text="Fetch Data", command=fetch_and_display).pack(pady=10)

root.mainloop()