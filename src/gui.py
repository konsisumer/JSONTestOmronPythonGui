import tkinter as tk
from tkinter import messagebox, filedialog
from utils.helpers import send_json_data
import random
import string
import qrcode
from PIL import Image, ImageTk

# Helper function to generate a random string
def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Helper function to append status messages
def append_status_message(message):
    status_label.config(text=message)

# Function to generate and display a QR code
def generate_qr_code():
    data = collect_input_data()
    global qr_image
    qr_content = ";".join(map(str, [
        data["A"], data["B"], data["C"], data["BoxType"], data["Orientation"],
        data["Smallbox"], data["La"], data["Lb"], data["Lc"], data["JobName"],
        data["Enable"], data["Chars"], data["Pos"], data["Corner"], data["Flap"],
        data["DistanceStart"], data["DistanceHeight"], data["Lines"], data["EmptyLines"],
        data["NumMatrices"], data["Sheets"]
    ]))
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(qr_content)
    qr.make(fit=True)
    qr_image = qr.make_image(fill="black", back_color="white")
    qr_image_resized = qr_image.resize((200, 200))
    qr_photo = ImageTk.PhotoImage(qr_image_resized)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo
    append_status_message(f"QR code generated for: {data['JobName']}")

# Function to save the QR code as an image
def save_qr_code():
    if qr_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            qr_image.save(file_path)
            append_status_message(f"QR code saved to {file_path}")

# Function to copy the QR code to the clipboard
def copy_qr_code():
    if qr_image:
        qr_image_copy = qr_image.copy()
        qr_image_copy.show()
        append_status_message("QR code copied to clipboard (image viewer opened).")

# Function to collect input data
def collect_input_data():
    return {
        "JobName": entry_name.get(),
        "A": float(entry_a.get()),
        "B": float(entry_b.get()),
        "C": float(entry_c.get()),
        "BoxType": int(entry_type.get()),
        "Orientation": bool(var_orientation.get()),
        "Smallbox": bool(var_smallbox.get()),
        "La": int(entry_la.get()),
        "Lb": int(entry_lb.get()),
        "Lc": int(entry_lc.get()),
        "Enable": bool(var_braille.get()),
        "Chars": int(entry_chars.get()),
        "Pos": int(entry_braille_pos.get()),
        "Corner": int(entry_corner.get()),
        "Flap": int(entry_flap.get()),
        "DistanceStart": int(entry_distance_start.get()),
        "DistanceHeight": int(entry_distance_height.get()),
        "Lines": int(entry_lines.get()),
        "EmptyLines": int(entry_empty_lines.get()),
        "NumMatrices": int(entry_num_matrices.get()),
        "Sheets": int(entry_sheet.get())
    }

# Function to send data
def send_data():
    try:
        data = collect_input_data()
        url = entry_url.get()
        response_message = send_json_data(url, data)
        append_status_message(response_message)
        generate_qr_code()
    except ValueError as e:
        append_status_message(f"Error: Invalid input - {e}")
    except Exception as e:
        append_status_message(f"Error: Request failed - {e}")

# Function to toggle visibility of Braille-related fields
def toggle_braille_fields():
    widgets = [
        (label_chars, entry_chars), (label_braille_pos, entry_braille_pos),
        (label_corner, entry_corner), (label_flap, entry_flap),
        (label_distance_start, entry_distance_start), (label_distance_height, entry_distance_height),
        (label_lines, entry_lines), (label_empty_lines, entry_empty_lines),
        (label_num_matrices, entry_num_matrices)
    ]
    for label, entry in widgets:
        if var_braille.get():
            label.grid()
            entry.grid()
        else:
            label.grid_remove()
            entry.grid_remove()

# Helper function to create labeled entry fields
def create_labeled_entry(parent, label_text, default_value, row, column, width=10):
    label = tk.Label(parent, text=label_text)
    label.grid(row=row, column=column, padx=5, pady=5, sticky="w")
    entry = tk.Entry(parent, width=width)
    entry.insert(0, default_value)
    entry.grid(row=row, column=column + 1, padx=5, pady=5, sticky="w")
    return label, entry

# Create GUI
root = tk.Tk()
root.title("JSON Data Viewer")
root.geometry("1000x900")

# URL Input Section
url_frame = tk.Frame(root, padx=10, pady=10)
url_frame.pack(fill="x")
tk.Label(url_frame, text="URL:").grid(row=0, column=0, sticky="w")
entry_url = tk.Entry(url_frame, width=50)
entry_url.grid(row=0, column=1, padx=5)
entry_url.insert(0, "http://192.168.250.1:8090/")

# Input Fields Section
input_frame = tk.LabelFrame(root, text="Input Fields", padx=10, pady=10)
input_frame.pack(fill="x", padx=10, pady=10)

# Left Column
_, entry_a = create_labeled_entry(input_frame, "A:", "80.0", 0, 0)
_, entry_b = create_labeled_entry(input_frame, "B:", "25.0", 1, 0)
_, entry_c = create_labeled_entry(input_frame, "C:", "15.0", 2, 0)
_, entry_type = create_labeled_entry(input_frame, "TYPE:", "1", 3, 0)

tk.Label(input_frame, text="ORIENTATION:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
var_orientation = tk.IntVar(value=0)
checkbox_orientation = tk.Checkbutton(input_frame, variable=var_orientation)
checkbox_orientation.grid(row=4, column=1, padx=5, pady=5, sticky="w")

tk.Label(input_frame, text="SMALLBOX:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
var_smallbox = tk.IntVar(value=0)
checkbox_smallbox = tk.Checkbutton(input_frame, variable=var_smallbox)
checkbox_smallbox.grid(row=5, column=1, padx=5, pady=5, sticky="w")

_, entry_la = create_labeled_entry(input_frame, "La:", "190", 6, 0)
_, entry_lb = create_labeled_entry(input_frame, "Lb:", "150", 7, 0)
_, entry_lc = create_labeled_entry(input_frame, "Lc:", "110", 8, 0)
_, entry_name = create_labeled_entry(input_frame, "NAME:", generate_random_string(), 9, 0, width=30)
_, entry_sheet = create_labeled_entry(input_frame, "SHEETS:", "10000", 10, 0)

# Right Column
tk.Label(input_frame, text="Braille:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
var_braille = tk.IntVar(value=0)
checkbox_braille = tk.Checkbutton(input_frame, variable=var_braille, command=toggle_braille_fields)
checkbox_braille.grid(row=0, column=3, padx=5, pady=5, sticky="w")

label_chars, entry_chars = create_labeled_entry(input_frame, "Chars:", "16", 1, 2)
label_braille_pos, entry_braille_pos = create_labeled_entry(input_frame, "BraillePos:", "1", 2, 2)
label_corner, entry_corner = create_labeled_entry(input_frame, "Corner:", "1", 3, 2)
label_flap, entry_flap = create_labeled_entry(input_frame, "Flap:", "1", 4, 2)
label_distance_start, entry_distance_start = create_labeled_entry(input_frame, "DistanceStart:", "8", 5, 2)
label_distance_height, entry_distance_height = create_labeled_entry(input_frame, "DistanceHeight:", "8", 6, 2)
label_lines, entry_lines = create_labeled_entry(input_frame, "Lines:", "2", 7, 2)
label_empty_lines, entry_empty_lines = create_labeled_entry(input_frame, "EmptyLines:", "0", 8, 2)
label_num_matrices, entry_num_matrices = create_labeled_entry(input_frame, "NumMatrices:", "2", 9, 2)

# Initially hide Braille-related fields and their labels
toggle_braille_fields()

# QR Code Section
qr_frame = tk.LabelFrame(root, text="QR Code", padx=10, pady=10)
qr_frame.pack(fill="x", padx=10, pady=10)
qr_label = tk.Label(qr_frame)
qr_label.pack()

tk.Button(qr_frame, text="Generate QR Code", command=generate_qr_code).pack(side="left", padx=5)
tk.Button(qr_frame, text="Save QR Code", command=save_qr_code).pack(side="left", padx=5)
tk.Button(qr_frame, text="Copy QR Code", command=copy_qr_code).pack(side="left", padx=5)

# Status Section (Status Bar)
status_frame = tk.Frame(root, padx=10, pady=5)
status_frame.pack(fill="x", side="bottom")
status_label = tk.Label(status_frame, text="Ready", anchor="w", relief="sunken", padx=5)
status_label.pack(fill="x")

# Send Data Button
tk.Button(root, text="Send Data", command=send_data).pack(pady=10)

root.mainloop()