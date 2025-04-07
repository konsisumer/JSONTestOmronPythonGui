import tkinter as tk
from tkinter import messagebox, filedialog
from utils.helpers import send_json_data
import random
import string
import qrcode
from PIL import Image, ImageTk

# Helper function to generate a random string
def generate_random_string(length=10):
    """Generate a random string of the specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Helper function to append status messages
def append_status_message(message):
    """Update the status message in the status bar."""
    status_label.config(text=message)

# Function to generate and display a QR code
def generate_qr_code(data):
    """Generate a QR code from the given data and display it in the GUI."""
    global qr_image  # Keep a reference to the QR code image for saving
    qr_content = f"{data['A']};{data['B']};{data['C']};{data['BoxType']};{data['Orientation']};{data['Smallbox']};{data['La']};{data['Lb']};{data['Lc']};{data['JobName']};{data['Enable']};{data['Chars']};{data['Pos']};{data['Corner']};{data['Flap']};{data['DistanceStart']};{data['DistanceHeight']};{data['Lines']};{data['EmptyLines']};{data['NumMatrices']}"
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(qr_content)
    qr.make(fit=True)
    qr_image = qr.make_image(fill="black", back_color="white")
    qr_image_resized = qr_image.resize((200, 200))  # Resize for display in the GUI
    qr_photo = ImageTk.PhotoImage(qr_image_resized)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo  # Keep a reference to avoid garbage collection

# Function to save the QR code as an image
def save_qr_code():
    """Save the QR code as an image file."""
    if qr_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            qr_image.save(file_path)
            append_status_message(f"QR code saved to {file_path}")

# Function to copy the QR code to the clipboard
def copy_qr_code():
    """Copy the QR code to the clipboard."""
    if qr_image:
        qr_image_copy = qr_image.copy()
        qr_image_copy.show()  # This opens the image in the default viewer, simulating a copy action
        append_status_message("QR code copied to clipboard (image viewer opened).")

# Function to send data
def send_data():
    try:
        data = {
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
            "NumMatrices": int(entry_num_matrices.get())
        }
        url = entry_url.get()
        response_message = send_json_data(url, data)
        append_status_message(response_message)

        # Generate and display the QR code
        generate_qr_code(data)
    except ValueError as e:
        append_status_message(f"Error: Invalid input - {e}")
    except Exception as e:
        append_status_message(f"Error: Request failed - {e}")

# Function to toggle visibility of Braille-related fields
def toggle_braille_fields():
    if var_braille.get():
        # Show Braille-related fields and their labels
        label_chars.grid()
        entry_chars.grid()
        label_braille_pos.grid()
        entry_braille_pos.grid()
        label_corner.grid()
        entry_corner.grid()
        label_flap.grid()
        entry_flap.grid()
        label_distance_start.grid()
        entry_distance_start.grid()
        label_distance_height.grid()
        entry_distance_height.grid()
        label_lines.grid()
        entry_lines.grid()
        label_empty_lines.grid()
        entry_empty_lines.grid()
        label_num_matrices.grid()
        entry_num_matrices.grid()
    else:
        # Hide Braille-related fields and their labels
        label_chars.grid_remove()
        entry_chars.grid_remove()
        label_braille_pos.grid_remove()
        entry_braille_pos.grid_remove()
        label_corner.grid_remove()
        entry_corner.grid_remove()
        label_flap.grid_remove()
        entry_flap.grid_remove()
        label_distance_start.grid_remove()
        entry_distance_start.grid_remove()
        label_distance_height.grid_remove()
        entry_distance_height.grid_remove()
        label_lines.grid_remove()
        entry_lines.grid_remove()
        label_empty_lines.grid_remove()
        entry_empty_lines.grid_remove()
        label_num_matrices.grid_remove()
        entry_num_matrices.grid_remove()

# Helper function to create labeled entry fields
def create_labeled_entry(parent, label_text, default_value, row, column, width=10):
    tk.Label(parent, text=label_text).grid(row=row, column=column, padx=5, pady=5, sticky="w")
    entry = tk.Entry(parent, width=width)
    entry.insert(0, default_value)
    entry.grid(row=row, column=column + 1, padx=5, pady=5, sticky="w")
    return entry

# Create GUI
root = tk.Tk()
root.title("JSON Data Viewer")
root.geometry("900x800")

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
entry_a = create_labeled_entry(input_frame, "A:", "80.0", 0, 0)
entry_b = create_labeled_entry(input_frame, "B:", "25.0", 1, 0)
entry_c = create_labeled_entry(input_frame, "C:", "15.0", 2, 0)
entry_type = create_labeled_entry(input_frame, "TYPE:", "1", 3, 0)

tk.Label(input_frame, text="ORIENTATION:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
var_orientation = tk.IntVar(value=0)
checkbox_orientation = tk.Checkbutton(input_frame, variable=var_orientation)
checkbox_orientation.grid(row=4, column=1, padx=5, pady=5, sticky="w")

tk.Label(input_frame, text="SMALLBOX:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
var_smallbox = tk.IntVar(value=0)
checkbox_smallbox = tk.Checkbutton(input_frame, variable=var_smallbox)
checkbox_smallbox.grid(row=5, column=1, padx=5, pady=5, sticky="w")

entry_la = create_labeled_entry(input_frame, "La:", "190", 6, 0)
entry_lb = create_labeled_entry(input_frame, "Lb:", "150", 7, 0)
entry_lc = create_labeled_entry(input_frame, "Lc:", "110", 8, 0)

entry_name = create_labeled_entry(input_frame, "NAME:", generate_random_string(), 9, 0, width=30)

# Right Column
tk.Label(input_frame, text="Braille:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
var_braille = tk.IntVar(value=0)
checkbox_braille = tk.Checkbutton(input_frame, variable=var_braille, command=toggle_braille_fields)
checkbox_braille.grid(row=0, column=3, padx=5, pady=5, sticky="w")

# Braille-related fields (initially hidden)
label_chars = tk.Label(input_frame, text="Chars:")
label_chars.grid(row=1, column=2, padx=5, pady=5, sticky="w")
entry_chars = tk.Entry(input_frame, width=10)
entry_chars.insert(0, "16")
entry_chars.grid(row=1, column=3, padx=5, pady=5, sticky="w")

label_braille_pos = tk.Label(input_frame, text="BraillePos:")
label_braille_pos.grid(row=2, column=2, padx=5, pady=5, sticky="w")
entry_braille_pos = tk.Entry(input_frame, width=10)
entry_braille_pos.insert(0, "1")
entry_braille_pos.grid(row=2, column=3, padx=5, pady=5, sticky="w")

label_corner = tk.Label(input_frame, text="Corner:")
label_corner.grid(row=3, column=2, padx=5, pady=5, sticky="w")
entry_corner = tk.Entry(input_frame, width=10)
entry_corner.insert(0, "1")
entry_corner.grid(row=3, column=3, padx=5, pady=5, sticky="w")

label_flap = tk.Label(input_frame, text="Flap:")
label_flap.grid(row=4, column=2, padx=5, pady=5, sticky="w")
entry_flap = tk.Entry(input_frame, width=10)
entry_flap.insert(0, "1")
entry_flap.grid(row=4, column=3, padx=5, pady=5, sticky="w")

label_distance_start = tk.Label(input_frame, text="DistanceStart:")
label_distance_start.grid(row=5, column=2, padx=5, pady=5, sticky="w")
entry_distance_start = tk.Entry(input_frame, width=10)
entry_distance_start.insert(0, "8")
entry_distance_start.grid(row=5, column=3, padx=5, pady=5, sticky="w")

label_distance_height = tk.Label(input_frame, text="DistanceHeight:")
label_distance_height.grid(row=6, column=2, padx=5, pady=5, sticky="w")
entry_distance_height = tk.Entry(input_frame, width=10)
entry_distance_height.insert(0, "8")
entry_distance_height.grid(row=6, column=3, padx=5, pady=5, sticky="w")

label_lines = tk.Label(input_frame, text="Lines:")
label_lines.grid(row=7, column=2, padx=5, pady=5, sticky="w")
entry_lines = tk.Entry(input_frame, width=10)
entry_lines.insert(0, "2")
entry_lines.grid(row=7, column=3, padx=5, pady=5, sticky="w")

label_empty_lines = tk.Label(input_frame, text="EmptyLines:")
label_empty_lines.grid(row=8, column=2, padx=5, pady=5, sticky="w")
entry_empty_lines = tk.Entry(input_frame, width=10)
entry_empty_lines.insert(0, "0")
entry_empty_lines.grid(row=8, column=3, padx=5, pady=5, sticky="w")

label_num_matrices = tk.Label(input_frame, text="NumMatrices:")
label_num_matrices.grid(row=9, column=2, padx=5, pady=5, sticky="w")
entry_num_matrices = tk.Entry(input_frame, width=10)
entry_num_matrices.insert(0, "2")
entry_num_matrices.grid(row=9, column=3, padx=5, pady=5, sticky="w")

# Initially hide Braille-related fields and their labels
toggle_braille_fields()

# QR Code Section
qr_frame = tk.LabelFrame(root, text="QR Code", padx=10, pady=10)
qr_frame.pack(fill="x", padx=10, pady=10)
qr_label = tk.Label(qr_frame)
qr_label.pack()

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